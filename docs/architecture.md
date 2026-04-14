# AI Meeting Presentation Agent - Architecture

```mermaid
graph TD
    A[Meeting Transcript] --> B[MeetingAnalyzer]
    B --> C{LLM: GPT-4o-mini}
    C --> D[Structured Analysis]
    D --> E[Placeholder Mapping]
    E --> F[SlidesManager]
    F --> G[Google Slides Template]
    G --> H[New Analysis Presentation]
    
    subgraph "Core Components"
    B
    F
    end
    
    subgraph "Integrations"
    C
    G
    end
```

## Workflow Overview
1. **Extraction**: The CLI reads the raw transcript file.
2. **Analysis**: The `MeetingAnalyzer` uses OpenAI's Structured Outputs to extract a `MeetingAnalysis` Pydantic model.
3. **Mappig**: Analysis data is mapped to specific placeholders like `{{TITLE}}`, `{{EXEC_BULLET_1}}`, etc.
4. **Generation**: `SlidesManager` clones the Google Slides template and performs a `batchUpdate` to create the final deck.
