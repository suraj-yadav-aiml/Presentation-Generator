

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage, HumanMessage
from typing import Dict, Any

from src.presentation_generation.utility import Slides
from src.presentation_generation.state import PresentationState

class OrchestratorNode:
    def __init__(self, llm: BaseChatModel):
        self.llm = llm
        self.presentation_planner = self.llm.with_structured_output(Slides)
    
    def orchestrator_node(self, state: PresentationState):
 
        presentation_topic = state.get('topic', '')
        number_of_slides = state.get('no_of_slides', 10)
        audience = state.get('audience', 'General audience')
        tone = state.get('tone', 'Professional')
        presentation_style = state.get('presentation_style', 'Business')
        presentation_purpose = state.get('presentation_purpose', 'Inform/Educate')
        special_instructions = state.get('special_instructions', '')
        
        # Create optimized system message
        system_message = SystemMessage(
            content=(
                "You are an expert presentation designer specializing in creating professional, "
                "engaging, and visually appealing slide decks. Your expertise includes crafting "
                "presentations for various industries, audiences, and purposes. Your slides have "
                "clear, concise content with a logical flow, maintaining a consistent tone and style. "
                "You're skilled at translating complex topics into digestible visual presentations."
            )
        )
        
        human_message = HumanMessage(
            content=(
                f"Create a detailed {number_of_slides}-slide presentation on the topic: '{presentation_topic}'\n\n"
                f"AUDIENCE: The presentation is for {audience}\n"
                f"TONE: Use a {tone} tone throughout the presentation\n"
                f"STYLE: Format as a {presentation_style} presentation\n"
                f"PURPOSE: The main goal is to {presentation_purpose}\n"
                "INSTRUCTIONS:\n"
                "1. Create a logical flow from introduction to conclusion\n"
                "2. Include specific, concrete visual suggestions for each slide\n"
                "3. Use concise bullet points with actual content, not placeholders\n"
                "4. Ensure slides are not text-heavy (limit text per slide)\n"
                "5. Include speaker notes with expanded talking points\n"
                f"6. Additional requirements: {special_instructions}\n\n"
                "For each slide, provide:\n"
                "- A clear slide title\n"
                "- Slide content (bullets, key points)\n"
                "- Visual suggestion (chart type, image concept, layout)\n"
                "- Brief speaker notes"
            )
        )
        
        presentation_slides = self.presentation_planner.invoke(
            input=[system_message, human_message]
        )
        
        return {
            'slides': presentation_slides.slides
        }
    
