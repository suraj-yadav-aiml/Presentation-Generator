from langgraph.constants import Send
from typing import List, Dict, Any, Callable
from src.presentation_generation.state import PresentationState
from src.presentation_generation.utility import Slide


class SlideWorkerEdge:
    
    def assign_slide_worker_agent(self, state: PresentationState):

        slides: List[Slide] = state.get('slides', [])
        
        if not slides:
            st.error("No slides to process.")
            return []
        
        # context = {
        #     'audience': state.get('audience', ''),
        #     'tone': state.get('tone', ''),
        #     'presentation_style': state.get('presentation_style', ''),
        #     'presentation_purpose': state.get('presentation_purpose', ''),
        #     'special_instructions': state.get('special_instructions', '')
        # }
        
        # worker_tasks = []
        # for slide in slides:
        #     task_args = {
        #         'slide': slide,
        #     }
        #     task_args.update(context)
        #     worker_tasks.append(Send(node="slide_worker_agent", arg=task_args))
        
        # return worker_tasks

        # return [Send(node="slide_worker_agent", arg={'slide': slide}.update(context)) for slide in slides]

        return [Send(
            node = "slide_worker_agent",
            arg = {
                'audience': state.get('audience', ''),
                'tone': state.get('tone', ''),
                'presentation_style': state.get('presentation_style', ''),
                'presentation_purpose': state.get('presentation_purpose', ''),
                'special_instructions': state.get('special_instructions', ''),
                'slide': slide
            }
        )
            for slide in slides
        ]