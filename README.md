#  Agentic AI Labs

A practical collection of **Agentic AI laboratory implementations** exploring how Large Language Models (LLMs) can reason, use tools, retrieve information, maintain memory, interact with humans, and collaborate through multi-agent systems.

This repository contains hands-on implementations using modern AI frameworks and technologies including **LangChain, LangGraph, AutoGen, ChromaDB, FAISS, SQLite, and LangSmith**.

---

##  Overview

The labs in this repository progressively explore different concepts involved in building intelligent AI agents.

The implementations cover:

-  LLM Agents & Tool Calling
-  Conversational Memory
-  LangGraph Workflows
-  Human-in-the-Loop (HITL)
-  Retrieval-Augmented Generation (RAG)
-  Advanced RAG & Query Reformulation
-  Multi-Agent Systems
-  Persistent Agent Memory
-  Supervisor–Worker Architectures
-  Agent Tracing & Evaluation
-  Multi-Step AI Workflows
-  Vector Databases

---

## 🧪 Lab Contents

| #      | Lab                           | Description                                                                                                        |
| ------ | ----------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **01** | `1_agent_with_tools.py`       | A ReAct-style agent that uses **Wikipedia** and a **Calculator** as external tools.                                |
| **02** | `2_langgraph_chatbot.py`      | A conversational chatbot built with **LangGraph**, demonstrating state and conversational memory.                  |
| **03** | `3_hitl_email_agent.py`       | A **Human-in-the-Loop** agent that iteratively drafts and improves professional emails with human feedback.        |
| **04** | `4_chroma_rag_pdf_qa.py`      | A basic **RAG-based PDF Question Answering** system using **ChromaDB** as the vector store.                        |
| **05** | `5_advanced_rag_pdf.py`       | An advanced RAG system capable of **reformulating queries** when an appropriate answer cannot initially be found.  |
| **06** | `6_autogen_writer_agent.py`   | A **multi-agent system** using AutoGen with separate Writer and Critic agents.                                     |
| **07** | `7_sqlite_memory_agent.py`    | An agent that stores conversational facts persistently using an **SQLite database**.                               |
| **08** | `8_langgraph_team_agent.py`   | A LangGraph-based **Supervisor–Worker architecture** featuring a Supervisor agent and a mathematical Worker agent. |
| **09** | `9_langsmith_agent.py`        | An agent demonstrating **tracing, monitoring, and evaluation** using LangSmith.                                    |
| **10** | `10_duckduckgo_news_agent.py` | A multi-step news aggregation workflow using **DuckDuckGo search, summarization, and report generation**.          |
| —      | `rag.py`                      | A RAG implementation using **FAISS** for vector similarity search.                                                 |

---

##  Concepts Covered

### 1. LLM Agents

Learn how LLMs can go beyond generating text by deciding when and how to use external tools.

The first lab demonstrates an agent capable of selecting appropriate tools such as:

- Wikipedia search
- Calculator
- LLM reasoning
- Tool execution

---

### 2. Conversational Memory

Agents often need to remember previous interactions to maintain meaningful conversations.

The LangGraph chatbot demonstrates how conversational state can be maintained across multiple interactions.

---

### 3. Human-in-the-Loop

Not every AI decision should be completely autonomous.

The HITL email agent demonstrates a workflow where:

1. The agent generates a draft.
2. A human reviews the output.
3. Feedback is provided.
4. The agent improves the draft.
5. The process continues until the desired result is achieved.

---

### 4. Retrieval-Augmented Generation (RAG)

RAG allows an LLM to retrieve relevant information from external documents before generating an answer.

The RAG implementations demonstrate:

**Documents → Chunking → Embeddings → Vector Store → Retrieval → LLM Response**

The repository explores RAG using:

- ChromaDB
- FAISS
- PDF documents
- Query retrieval
- Query reformulation

---

### 5. Multi-Agent Systems

Complex tasks can be divided among multiple specialized agents.

The AutoGen implementation demonstrates collaboration between:

- **Writer Agent** — generates content
- **Critic Agent** — reviews and provides feedback

This introduces the concept of agents working together instead of relying on a single agent.

---

### 6. Persistent Memory

The SQLite memory agent demonstrates how an AI system can store information beyond a single conversation.

SQLite is used to persist conversational facts so that the agent can retrieve them in future interactions.

---

### 7. Supervisor–Worker Architecture

The LangGraph team agent demonstrates a hierarchical multi-agent architecture.

The system contains:

- **Supervisor Agent** — decides which agent should handle the task
- **Worker Agent** — performs the assigned task

This architecture can be extended to systems containing multiple specialized workers.

---

### 8. Agent Observability & Evaluation

The LangSmith lab demonstrates how agent applications can be monitored and evaluated.

This is important for understanding:

- Agent execution
- LLM calls
- Tool calls
- Intermediate steps
- Errors
- Performance
- Evaluation results

---

### 9. Multi-Step AI Workflows

The DuckDuckGo news agent demonstrates how multiple AI steps can be connected into a workflow:

**Search → Collect Information → Summarize → Generate Report**

This introduces the idea of building structured pipelines rather than relying on a single LLM call.

---

## 🛠️ Technologies Used

### AI & Agent Frameworks

- **LangChain**
- **LangGraph**
- **AutoGen**

### Vector Databases

- **ChromaDB**
- **FAISS**

### Memory & Storage

- **SQLite**

### Observability & Evaluation

- **LangSmith**

### Search

- **DuckDuckGo**

### Programming Language

- **Python**

### Model Provider

- **Groq API**

---

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

> Some individual labs may also contain their own dependency installation instructions, particularly when they are designed to run inside Jupyter notebooks.

---

##  API Key Configuration

The labs require a **Groq API key** to access the language models.

Create an environment variable named:

```text
GROQ_API_KEY
```

### Windows PowerShell

```powershell
$env:GROQ_API_KEY="your_api_key_here"
```

### macOS / Linux

```bash
export GROQ_API_KEY="your_api_key_here"
```

Alternatively, you can use a `.env` file if the implementation is configured to load environment variables through `python-dotenv`.

Example:

```env
GROQ_API_KEY=your_api_key_here
```

 **Never commit your API keys or `.env` files containing secrets to GitHub.**

---

##  Running the Labs

Each lab is implemented as a separate Python file.

For example:

```bash
python 1_agent_with_tools.py
```

To run another lab:

```bash
python 4_chroma_rag_pdf_qa.py
```

```bash
python 6_autogen_writer_agent.py
```

```bash
python 8_langgraph_team_agent.py
```

The exact requirements may vary between labs depending on the framework and external services being used.

---

## 📂 Project Structure

```text
Agentic-AI-Labs/
---- Agentic AI Labs 1 - 10.ipynb
├── 1_agent_with_tools.py
├── 2_langgraph_chatbot.py
├── 3_hitl_email_agent.py
├── 4_chroma_rag_pdf_qa.py
├── 5_advanced_rag_pdf.py
├── 6_autogen_writer_agent.py
├── 7_sqlite_memory_agent.py
├── 8_langgraph_team_agent.py
├── 9_langsmith_agent.py
├── 10_duckduckgo_news_agent.py
├── rag.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Learning Path

The labs can be followed in the following order:

```text
LLM Agents
     ↓
Tool Calling
     ↓
Conversational Memory
     ↓
Human-in-the-Loop
     ↓
Basic RAG
     ↓
Advanced RAG
     ↓
Multi-Agent Systems
     ↓
Persistent Memory
     ↓
Supervisor–Worker Agents
     ↓
Agent Observability
     ↓
Multi-Step AI Workflows
```

This progression moves from fundamental agent concepts toward more advanced agentic architectures.

---

##  Learning Objectives

By completing these labs, you will gain practical experience with:

- Building LLM-powered agents
- Connecting agents to external tools
- Managing conversational state
- Designing Human-in-the-Loop workflows
- Building RAG pipelines
- Working with vector databases
- Improving retrieval through query reformulation
- Creating collaborative multi-agent systems
- Implementing persistent memory
- Designing supervisor–worker architectures
- Monitoring and evaluating AI agents
- Building multi-step autonomous workflows

---

##  Notes

- A valid **Groq API key** is required for the model-powered labs.
- Some labs may require additional API keys or external services depending on their configuration.
- API keys should never be hard-coded into source files.
- Vector databases may generate local files or directories when running RAG implementations.
- Make sure required dependencies are installed before executing each lab.
- Some implementations may require a PDF or other input data to be available locally.

---

##  Course Focus

This repository focuses on the practical implementation of **Agentic AI concepts**, moving beyond basic LLM prompting toward systems capable of:

**Reasoning → Tool Use → Memory → Retrieval → Human Interaction → Collaboration → Autonomous Workflows**

---

##  Author

**Aneesh Rao S V**

B.Tech — Computer Science Engineering (AI & ML)

Garden City University, Bengaluru

---

⭐ If you find this repository useful for learning Agentic AI, consider giving it a star!
