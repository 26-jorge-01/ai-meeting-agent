import os
import json
from typing import Dict, Any
from openai import OpenAI
from .models import MeetingAnalysis, PresentationStructure, SlideContent

class MeetingAnalyzer:
    def __init__(self, api_key: str = None):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    def analyze_transcript(self, transcript: str) -> MeetingAnalysis:
        """Analyzes a meeting transcript and extracts structured information."""
        prompt = f"""
        You are an expert executive assistant. Analyze the following meeting transcript and extract:
        1. High-level summary.
        2. Key meeting objectives.
        3. Action items (including task, owner, due date, and priority if available).
        4. Next steps.
        5. Overall sentiment.

        Transcript:
        {transcript}
        """
        
        response = self.client.beta.chat.completions.parse(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional business analyst."},
                {"role": "user", "content": prompt}
            ],
            response_format=MeetingAnalysis
        )
        return response.choices[0].message.parsed

    def prepare_presentation_data(self, analysis: MeetingAnalysis) -> Dict[str, str]:
        """Maps the meeting analysis to the specific placeholders in the Google Slides template."""
        
        # Initialize placeholders map
        placeholders = {
            "{{TITLE}}": "Meeting Insights",
            "{{SUBTITLE}}": analysis.summary[:100] + "..." if len(analysis.summary) > 100 else analysis.summary
        }

        # Executive Summary (Slide 2)
        for i in range(1, 4):
            val = analysis.action_items[i-1] if len(analysis.action_items) >= i else ""
            placeholders[f"{{{{EXEC_BULLET_{i}}}}}] = val

        # Objectives (Slide 3)
        for i in range(1, 4):
            val = analysis.objectives[i-1] if len(analysis.objectives) >= i else ""
            placeholders[f"{{{{OBJ_{i}}}}}] = val

        # Action Items (Slide 4) - Simplified mapping for the test
        # In a real scenario, we'd parse tasks/owners more granularly
        for i in range(1, 4):
            if len(analysis.action_items) >= i:
                item = analysis.action_items[i-1]
                placeholders[f"{{{{ACTION_{i}_TASK}}}}"] = item
                placeholders[f"{{{{ACTION_{i}_OWNER}}}}"] = "TBD"
                placeholders[f"{{{{ACTION_{i}_DUE}}}}"] = "TBD"
                placeholders[f"{{{{ACTION_{i}_PRIORITY}}}}"] = "High"
            else:
                placeholders[f"{{{{ACTION_{i}_TASK}}}}"] = ""
                placeholders[f"{{{{ACTION_{i}_OWNER}}}}"] = ""
                placeholders[f"{{{{ACTION_{i}_DUE}}}}"] = ""
                placeholders[f"{{{{ACTION_{i}_PRIORITY}}}}"] = ""

        # Next Steps (Slide 5)
        for i in range(1, 6):
            val = analysis.next_steps[i-1] if len(analysis.next_steps) >= i else ""
            placeholders[f"{{{{NEXT_{i}}}}}] = val

        return placeholders
