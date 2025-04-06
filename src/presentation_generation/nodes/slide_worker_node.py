
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import SystemMessage, HumanMessage
from typing import Dict, Any, List
from src.presentation_generation.state import SlideWorkerState
from src.presentation_generation.utility import Slide


class SlideWorkerNode:
    
    def __init__(self, llm: BaseChatModel):
        self.slide_writer = llm
    
    def slide_worker_node(self, state: SlideWorkerState):

        slide: Slide = state['slide']
        
        audience = state.get('audience', 'General audience')
        tone = state.get('tone', 'Professional')
        presentation_style = state.get('presentation_style', 'Business')
        presentation_purpose = state.get('presentation_purpose', 'Inform')
        special_instructions = state.get('special_instructions', '')
        
        system_prompt = (
            "You are an expert presentation designer. Generate professional slide content that:"
            f"\n1. Addresses a {audience} audience"
            f"\n2. Uses a {tone} tone of voice"
            f"\n3. Follows {presentation_style} presentation style"
            f"\n4. Serves the purpose to {presentation_purpose}"
            "\n5. Uses clear, concise bullet points (3-5 points maximum)"
            "\n6. Includes a visual suggestion labeled as [VISUAL: your suggestion]"
            "\n7. Adds brief speaker notes labeled as [NOTES: your notes]"
            "\n8. Maintains consistency with presentation best practices"
        )
        
        if special_instructions:
            system_prompt += f"\n9. Special requirements: {special_instructions}"
        
        human_prompt = (
            f"Create a complete slide with title: \"{slide.title}\"\n\n"
            f"Key points to cover: {slide.description}\n\n"
            f"Format the content as bullet points, followed by a visual suggestion and speaker notes."
        )
        
        slide_content = self.slide_writer.invoke(
            input=[
                SystemMessage(content=system_prompt),
                HumanMessage(content=human_prompt)
            ]
        )
        
        return {
            'completed_slides': [slide_content.content]
        }