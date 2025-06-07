# Multi-Agent Feedback Loop Web App

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/streamlit-enabled-brightgreen.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview
This is a Streamlit-based interactive web application that leverages multiple autonomous AI agents to generate and critique responses to a user's query. The agents work independently and collaboratively in a feedback loop, enabling a richer and more critical multi-perspective analysis.

## Features
- Multiple AI agents generate diverse responses
- Peer evaluation system where agents review each other's output
- Modular architecture with extensibility for new tools or agent roles
- Lightweight and easy-to-deploy using Streamlit

## Core Concepts
This application implements a **multi-agent reasoning loop**:
1. **User enters a query**.
2. Multiple **response agents** generate answers.
3. One or more **evaluation agents** assess those answers based on criteria like accuracy, relevance, or creativity.
4. The evaluation helps highlight the most compelling responses or guide further refinement.

## Architecture
```bash
multi-agent-app/
├── agents/
│   ├── base_agent.py       # Abstract base class for all agents
│   └── evaluator.py        # Agent that evaluates generated responses
├── models/
│   └── model_loader.py     # Loads external LLMs
├── tools/
│   └── web_search.py       # Web search tool for agents needing context
├── main.py                 # Streamlit entry point
```

## External Libraries & Models Used
- **OpenAI API** (e.g., GPT-4) via `openai` library
- **Streamlit** for UI rendering
- **LangChain** for agent structuring and tools
- **Python Standard Libraries**: `abc`, `typing`, `os`, `dotenv`, etc.

## Installation & Setup
### 1. Clone the repository
```bash
git clone https://github.com/anshulraj10/multi-llm-agents-feedback.git
cd multi-llm-agents-feedback
```

### 2. Set up Python environment
We recommend Python 3.10 or later.
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add API keys
Create a `.env` file in the root directory:
```env
HF_ACCESS_TOKEN=your-huggingface-token-here
```

### 5. Run the app
```bash
streamlit run main.py
```

## Usage
- Open the app in your browser.
- Enter a query like: "What are the pros and cons of AI in education?"
- Review how each agent responds and how they critique one another.
- Use this tool to explore multi-faceted viewpoints or generate collaborative AI-driven content.

## Contribution Guidelines
Contributions are welcome! To contribute:
1. Fork the repository
2. Create your feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

## License
This project is licensed under the [MIT License](LICENSE).

## Credits and Acknowledgements
Developed by [Anshul Raj](https://anshulraj.com/)

Special thanks to the open-source community behind:
- [OpenAI](https://openai.com/)
- [LangChain](https://www.langchain.com/)
- [Streamlit](https://streamlit.io/)

---
> *This app demonstrates the power of collaborative reasoning through autonomous agents. Ideal for research, brainstorming, or prototyping decision-making systems.*
