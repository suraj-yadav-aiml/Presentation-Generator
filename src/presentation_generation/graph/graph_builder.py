import streamlit as st
import traceback
from langchain_core.language_models.chat_models import BaseChatModel
from langgraph.graph import START, END, StateGraph
from langgraph.graph.state import CompiledStateGraph

from src.presentation_generation.edges import SlideWorkerEdge
from src.presentation_generation.nodes import (
    OrchestratorNode,
    SlideWorkerNode,
    AggregatorNode
)

from src.presentation_generation.state import PresentationState

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.workflow = StateGraph(PresentationState)
    
    def _initialize_nodes(self) -> None:

        try:
            self.orchestrator_node = OrchestratorNode(self.llm).orchestrator_node
            self.slide_worker_node = SlideWorkerNode(self.llm).slide_worker_node
            self.aggregator_node = AggregatorNode().presentation_synthesizer_node
        
        except Exception as e:
            eerror_msg = f"Failed to initialize nodes: {str(e)}"
            st.error(error_msg)
            st.code(traceback.format_exc(), language="python")
            raise RuntimeError(error_msg)
    
    def _initialize_edges(self) -> None:
        try:
            self.slide_worker_edge = SlideWorkerEdge().assign_slide_worker_agent
        except Exception as e:
            error_msg = f"Failed to initialize edges: {str(e)}"
            st.error(error_msg)
            st.code(traceback.format_exc(), language="python")
            raise RuntimeError(error_msg)
    
    def _initialize_presentation_generation_graph(self) -> None:
        try:
            
            self.workflow.add_node("orchestrator", self.orchestrator_node)
            self.workflow.add_node("slide_worker_agent", self.slide_worker_node)
            self.workflow.add_node("presentation_synthesizer", self.aggregator_node)

            self.workflow.add_edge(START, "orchestrator")
            self.workflow.add_conditional_edges(
                "orchestrator",
                self.slide_worker_edge,
                ["slide_worker_agent"]
            )

            self.workflow.add_edge("slide_worker_agent", "presentation_synthesizer")
            self.workflow.add_edge("presentation_synthesizer", END)

        except Exception as e:
            error_msg = f"Failed to initialize presentation generation graph: {str(e)}"
            st.error(error_msg)
            st.code(traceback.format_exc(), language="python")
            raise RuntimeError(error_msg)

    def setup_graph(self) -> CompiledStateGraph:

        try:            
            
            self._initialize_nodes()
            self._initialize_edges()
            self._initialize_presentation_generation_graph()

            return self.workflow.compile()

        except Exception as e:
            error_msg = f"Failed to set up graph: {str(e)}"
            st.error(error_msg)
            st.code(traceback.format_exc(), language="python")
            raise RuntimeError(error_msg)


            


