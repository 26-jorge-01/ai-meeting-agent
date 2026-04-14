import os
import argparse
from dotenv import load_dotenv
from .analyzer import MeetingAnalyzer
from .presentation import SlidesManager

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="AI Meeting Presentation Agent")
    parser.add_argument("--transcript", type=str, required=True, help="Path to the meeting transcript file")
    parser.add_argument("--template_id", type=str, default="1vXhzzhoypMD2V5ayDzN0IB5RybMcGVAEx8XIoysc8qk", help="Google Slides Template ID")
    parser.add_argument("--output_title", type=str, default="Meeting Analysis Presentation", help="Title for the generated presentation")
    
    args = parser.parse_args()

    # 1. Initialize Analyzer and Slides Manager
    # Ensure OPENAI_API_KEY is in your .env
    analyzer = MeetingAnalyzer()
    
    # Ensure credentials.json is in the root directory for SlidesManager
    slides_manager = SlidesManager(credentials_path="credentials.json")

    # 2. Read Transcript
    print(f"Reading transcript from {args.transcript}...")
    with open(args.transcript, "r", encoding="utf-8") as f:
        transcript_text = f.read()

    # 3. Analyze Transcript
    print("Analyzing transcript using LLM...")
    analysis = analyzer.analyze_transcript(transcript_text)
    print("Analysis complete.")
    print(f"Summary: {analysis.summary[:100]}...")

    # 4. Prepare Placeholder Mappings
    print("Mapping analysis to slide placeholders...")
    placeholders = analyzer.prepare_presentation_data(analysis)

    # 5. Create Presentation
    print("Creating Google Slides presentation from template...")
    try:
        presentation_id = slides_manager.create_presentation_from_template(
            template_id=args.template_id,
            title=args.output_title
        )
        
        if presentation_id:
            print(f"New presentation created with ID: {presentation_id}")
            
            # 6. Replace Placeholders
            print("Updating slides with content...")
            slides_manager.replace_placeholders(presentation_id, placeholders)
            
            print("\n" + "="*50)
            print("SUCCESS: Presentation generated successfully!")
            print(f"URL: https://docs.google.com/presentation/d/{presentation_id}")
            print("="*50)
        else:
            print("FAILED: Could not create presentation copy.")
            
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("\nNote: Ensure 'credentials.json' is present and Authorized for Google Slides/Drive APIs.")

if __name__ == "__main__":
    main()
