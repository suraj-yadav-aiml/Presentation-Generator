# 🎯 Presentation Generator

A powerful AI-driven tool that automatically generates professional presentations based on user-defined topics, audience, and styling preferences.

## 📋 Project Overview

Presentation Generator is a streamlined web application that harnesses the capabilities of modern large language models (LLMs) to create comprehensive presentation outlines. The system uses a graph-based approach to orchestrate the generation process, breaking down complex presentations into individual slides that are processed in parallel before being aggregated into a cohesive final product.

### Key Features

- Multi-provider LLM support (Anthropic, OpenAI, Groq)
- Customizable presentation parameters (audience, tone, style, purpose)
- Flexible slide count and content density
- Streamlit-based user interface for easy interaction
- Download generated presentations as Markdown files
- Structured content with titles, bullet points, visual suggestions, and speaker notes

### Target Users

- Business professionals preparing presentations
- Educators creating lesson materials
- Researchers drafting conference talks
- Anyone seeking a quick starting point for presentation development

## 🔧 Technologies Used

- **Python**: Core programming language
- **LangChain & LangGraph**: For LLM orchestration and workflow management
- **Streamlit**: For the web-based user interface
- **LLM Integrations**:
  - OpenAI (GPT models)
  - Anthropic (Claude models)
  - Groq (Various models including Llama, Gemma, Qwen)
- **GitHub Actions**: For automated deployment to Hugging Face Spaces

## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- API keys for at least one of the supported LLM providers:
  - OpenAI API key
  - Anthropic API key
  - Groq API key

### Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/suraj-yadav-aiml/Presentation-Generator.git
   cd Presentation-Generator
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables for API keys (optional):
   ```bash
   # On Windows
   set OPENAI_API_KEY=your_openai_api_key
   set ANTHROPIC_API_KEY=your_anthropic_api_key
   set GROQ_API_KEY=your_groq_api_key
   
   # On macOS/Linux
   export OPENAI_API_KEY=your_openai_api_key
   export ANTHROPIC_API_KEY=your_anthropic_api_key
   export GROQ_API_KEY=your_groq_api_key
   ```

## 🚀 Usage

### Running the Application

1. Start the Streamlit application:
   ```bash
   python app.py
   ```
   
2. Open your browser and navigate to the URL displayed in the terminal (typically http://localhost:8501)

### Using the Interface

1. **Select LLM Provider**: Choose between Groq, OpenAI, or Anthropic
2. **Configure Provider Settings**: 
   - Enter your API key
   - Select a specific model
   - Adjust parameters like temperature and max tokens
3. **Define Presentation Details**:
   - Enter the presentation topic
   - Select target audience and tone
   - Specify number of slides
   - Choose presentation style and purpose
   - Add any special instructions
4. **Generate Presentation**: Click the "Generate Presentation" button
5. **View and Download**: Review the generated presentation and download it as a Markdown file



## 📁 Project Structure

```
📂 Presentation-Generation/
  📄 app.py                  # Application entry point
  📄 requirements.txt        # Project dependencies
  📂 src/                    # Source code directory
    📂 presentation_generation/
      📄 main.py             # Main application logic
      📂 edges/              # Graph edge definitions
      📂 graph/              # Graph builder and configuration
      📂 llm/                # LLM provider integrations
      📂 nodes/              # Graph node definitions
      📂 state/              # State management
      📂 ui/                 # User interface components
        📂 streamlit/        # Streamlit UI implementation
      📂 utility/            # Utility classes and functions
```

### Key Components

- **Graph Builder**: Constructs the workflow for presentation generation
- **Orchestrator Node**: Plans the overall presentation structure
- **Slide Worker Node**: Generates detailed content for individual slides
- **Aggregator Node**: Combines slide content into final presentation
- **LLM Providers**: Abstractions for different AI model APIs
- **UI Components**: Interface elements for user interaction

## 🔄 Workflow

1. The user inputs presentation details through the Streamlit UI
2. The Orchestrator Node creates a high-level outline with slide titles and descriptions
3. The Slide Worker Edge distributes slide generation tasks to the Slide Worker Node
4. The Slide Worker Node processes each slide, creating detailed content
5. The Aggregator Node combines all slides into a cohesive presentation
6. The result is displayed to the user with a download option

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

