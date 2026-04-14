# AI Meeting Presentation Agent

A production-grade automation tool that transforms meeting transcripts into polished executive presentations using LLMs and Google Slides.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI-green.svg)](https://openai.com/)

## 🚀 Overview

The **AI Meeting Presentation Agent** streamlines the post-meeting workflow by automatically analyzing transcripts and generating structured Google Slides. It uses GPT-4o-mini to extract key insights and maps them directly to a customizable slide template.

### Key Features
- **Intelligent Analysis**: Extracts summaries, objectives, action items, and next steps with high precision.
- **Dynamic Slide Generation**: Automated template copying and text replacement via Google Slides API.
- **Structured Data**: Uses Pydantic for robust data validation and OpenAI Structured Outputs.
- **Cost-Efficient**: Optimized for `gpt-4o-mini`, providing high quality at low cost.

## 🛠️ Architecture

The system follows a modular design:
- **`analyzer.py`**: Handles LLM orchestration and data mapping.
- **`presentation.py`**: Manages Google Slides/Drive API interactions.
- **`models.py`**: Defines the project's data schemas.

For more details, see [docs/architecture.md](docs/architecture.md).

## 📋 Setup

### Prerequisites
1. **OpenAI API Key**: Obtain from [OpenAI Platform](https://platform.openai.com/).
2. **Google Cloud Project**:
   - Enable **Google Slides API** and **Google Drive API**.
   - Create a **Service Account** and download the `credentials.json` file.
   - Share your Google Slides template with the Service Account email.

### Installation
```bash
git clone https://github.com/your-username/ai-meeting-agent.git
cd ai-meeting-agent
pip install -r requirements.txt
```

### Configuration
1. Rename `.env.example` to `.env` and add your OpenAI API Key.
2. Place your `credentials.json` in the project root.

## 🖥️ Usage

Run the agent via CLI:

```bash
python -m src.main --transcript samples/transcript.txt --output_title "Project Alpha Discovery Call"
```

## 📊 Cost Analysis (Estimate)
Based on current token pricing:
- **Meeting Analysis**: ~$0.01 per 10k words of transcript.
- **Total Workflow**: Negligible cost per presentation, making it highly scalable.

## 📜 License
Internal Technical Test Project.
