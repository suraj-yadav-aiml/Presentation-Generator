import streamlit as st
import traceback
from src.presentation_generation.ui.streamlit.loadui import StreamlitUILoader
from src.presentation_generation.ui.streamlit.display_result import DisplayResultStreamlit
from src.presentation_generation.llm import get_llm
from src.presentation_generation.graph import GraphBuilder




def presentation_creator():
    loader = StreamlitUILoader()
    user_input = loader.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    
    submit = st.button("Generate Presentation")

    if submit:
        try:
            llm = get_llm(provider=user_input['llm_provider'],
                        model_name=user_input['model_name'],
                        api_key=user_input['api_key'],
                        temperature=user_input['model_temperature'],
                        max_tokens=user_input['model_max_tokens'])
            

            graph = GraphBuilder(llm=llm).setup_graph()
            if graph is None:
                st.error("Error: Graph setup failed.")
                return

            DisplayResultStreamlit(graph, user_input).display_result_on_ui()
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.code(traceback.format_exc(), language="python")
        


    
    

    
