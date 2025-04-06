from typing import List
from src.presentation_generation.state import PresentationState


class AggregatorNode:

    def presentation_synthesizer_node(self,state: PresentationState):
        completed_slides: list[str] = state['completed_slides']
        if not completed_slides:
            return {
                'final_presentation': "No slides were generated.",
            }
            
        final_presentation = "\n\n--\n\n".join(completed_slides)

        return {
            'final_presentation': final_presentation
        }