from typing import List, Optional
from pydantic import BaseModel, Field

class SlideContent(BaseModel):
    title: str = Field(..., description="The title of the slide")
    bullets: List[str] = Field(default_factory=list, description="Bullet points for the slide content")
    placeholders: dict = Field(default_factory=dict, description="Key-Value pairs for slide placeholders, e.g., {'{{OBJECTIVE}}': 'Increase sales'}")

class MeetingAnalysis(BaseModel):
    summary: str = Field(..., description="A high-level summary of the meeting")
    objectives: List[str] = Field(..., description="List of meeting objectives identified")
    action_items: List[str] = Field(..., description="List of actionable tasks identified")
    next_steps: List[str] = Field(..., description="Follow-up actions and immediate next steps")
    sentiment: Optional[str] = Field(None, description="The overall sentiment of the meeting")

class PresentationStructure(BaseModel):
    presentation_title: str
    slides: List[SlideContent] = Field(..., description="The sequence of slides to be generated")
