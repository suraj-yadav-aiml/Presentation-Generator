from typing import List
from pydantic import BaseModel, Field


class Slide(BaseModel):
    """
    Represents a single slide in a presentation structure.
    
    This class defines the basic outline for an individual slide, consisting of a title
    and a description of key elements to be covered. This serves as a structural
    blueprint that will later be expanded into full slide content.
    """
    
    title: str = Field(
        description="The main heading or title that will appear at the top of the slide. "
                   "Should be concise, clear, and reflect the main point of the slide."
    )
    
    description: str = Field(
        description="Key elements and points to cover in this slide. This serves as an outline "
                   "of the important topics, bullet points, or concepts that should be included "
                   "when the full slide content is developed. This is not the final slide content "
                   "but rather a planning tool for content development."
    )


class Slides(BaseModel):
    """
    Represents a complete presentation structure containing multiple slides.
    
    This class serves as a container for a collection of Slide objects that
    together form the outline of a complete presentation. This outline can
    be used to generate the full presentation content.
    """
    
    slides: List[Slide] = Field(
        description="An ordered collection of slides that make up the presentation structure. "
                   "The order of slides determines the presentation flow, typically beginning "
                   "with an introduction, proceeding through main content points, and concluding "
                   "with a summary. Each slide contains a title and description of key points to cover."
    )