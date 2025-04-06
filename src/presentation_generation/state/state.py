from typing_extensions import TypedDict
from typing import List, Annotated
import operator
 
from src.presentation_generation.utility import Slide

class PresentationState(TypedDict):
    topic: str
    no_of_slides: int
    audience: str
    tone: str
    presentation_style: str
    presentation_purpose: str
    special_instructions: str
    slides: List[Slide]
    completed_slides: Annotated[List[str], operator.add]
    final_presentation: str

class SlideWorkerState(TypedDict):
    slide: Slide
    audience: str
    tone: str
    presentation_style: str
    presentation_purpose: str
    special_instructions: str
    completed_slides: Annotated[List[str], operator.add]