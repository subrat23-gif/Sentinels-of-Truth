**\# 🛡️ Sentinels of Truth**

An AI-powered Multi-Agent Claim Verification & Knowledge Management System built using \*\*LangGraph\*\*, \*\*Ollama\*\*, \*\*Streamlit\*\*, and \*\*SQLite\*\*.

This project simulates an automated fact-checking pipeline for a news agency where multiple AI agents collaborate to investigate claims, verify information using external search tools, and maintain a persistent knowledge base with contradiction handling.

\---

**\# 📌 Project Overview**

The system accepts an unverified claim from the user through a Streamlit web interface.

The claim then passes through a multi-agent workflow:

\- \*\*Agent Alpha (The Investigator / Scout)\*\* researches the claim using external web search and generates a structured verification report.

\- \*\*Agent Beta (The Archivist / Librarian)\*\* validates the report against an existing knowledge base and decides whether to:

\- INSERT new verified information

\- DISCARD redundant information

\- FLAG contradictory information for human review

The application demonstrates:

\- Multi-agent orchestration

\- Structured AI outputs

\- Persistent database storage

\- Contradiction detection

\- Uncertainty-aware reasoning

\- End-to-end AI workflow engineering

\---

**\# 🏗️ System Architecture**

\`\`\`text

User Claim

↓

Streamlit Frontend

↓

LangGraph Workflow

↓

Agent Alpha (Investigator)

↓

DuckDuckGo Search Tool

↓

Structured Verification Report

↓

Agent Beta (Archivist)

↓

SQLite Knowledge Base

↓

INSERT / DISCARD / FLAG

**🤖 Agents**

**🔎 Agent Alpha - The Investigator (Scout)**

**Responsibilities**

- Parses incoming claims
- Searches external information sources
- Generates structured verification reports
- Estimates confidence level
- Handles uncertain and ambiguous claims

**Tools**

- DuckDuckGo Search
- Ollama Local LLM
- Pydantic Structured Outputs

**Restrictions**

- Does NOT have database write access

**📚 Agent Beta - The Archivist (Librarian)**

**Responsibilities**

- Validates incoming reports
- Queries the persistent database
- Detects contradictions
- Prevents duplicate storage
- Maintains knowledge consistency

**Database Decisions**

| **Decision** | **Meaning**                  |
| ------------ | ---------------------------- |
| INSERTED     | New verified claim stored    |
| DISCARDED    | Duplicate claim detected     |
| FLAGGED      | Contradictory claim detected |

**⚙️ Technologies Used**

| **Technology**    | **Purpose**                 |
| ----------------- | --------------------------- |
| Python            | Core programming language   |
| Streamlit         | Frontend web application    |
| LangGraph         | Multi-agent orchestration   |
| Ollama            | Local LLM inference         |
| SQLite            | Persistent storage layer    |
| DuckDuckGo Search | External claim verification |
| Pydantic          | Structured LLM outputs      |

**🧠 Key Features**

- Multi-agent architecture
- LangGraph state orchestration
- Local LLM execution using Ollama
- Persistent SQLite knowledge base
- Structured verification reports
- Contradiction detection system
- Duplicate claim handling
- Uncertainty-aware reasoning
- Long-context claim processing
- Streamlit interactive UI

🗄️ **Database Schema**

The system uses SQLite as a persistent storage layer.

**Claims Table**

| **Column** | **Description**                |
| ---------- | ------------------------------ |
| id         | Unique claim ID                |
| claim      | User-submitted claim           |
| verdict    | Verification result            |
| reasoning  | Agent explanation              |
| confidence | Confidence score               |
| status     | INSERTED / DISCARDED / FLAGGED |
| timestamp  | Claim verification timestamp   |

**🔄 Workflow**

**1\. User Inputs Claim**

The user enters a claim through the Streamlit interface.

**2\. Agent Alpha Investigates**

- Searches external web data
- Analyzes claim validity
- Produces structured report:
  - verdict
  - reasoning
  - confidence

**3\. Agent Beta Validates**

- Queries database
- Checks existing records
- Performs contradiction detection

**4\. Final Decision**

The system returns:

- verification report
- database action
- final decision

**📋 Structured Output Example**

{

"verdict": "False",

"reasoning": "No credible scientific evidence supports the claim.",

"confidence": 0.87

}

**🚨 Edge Cases Tested**

The system was tested against multiple edge cases:

| **Edge Case**                 | **Status** |
| ----------------------------- | ---------- |
| Empty input                   | ✅         |
| Duplicate claims              | ✅         |
| Contradictory claims          | ✅         |
| Nonsense input                | ✅         |
| Ambiguous scientific claims   | ✅         |
| Long conspiracy-style prompts | ✅         |
| Structured output validation  | ✅         |

**▶️ How to Run**

**1\. Clone Repository**

git clone &lt;your-repository-url&gt;  
cd Sentinels-of-Truth

**2\. Install Dependencies**

pip install -r requirements.txt

**3\. Install Ollama**

Download and install Ollama:

<https://ollama.com>

**4\. Create Local Model**

ollama create agent_alpha -f Modelfile

**5\. Run Streamlit App**

streamlit run frontend.py

**🧪 Example Claims**

- The earth is flat
- Coffee is healthy
- Lentils are good for health
- A secret organization on Mars controls Earth's weather

**🔒 Design Decisions**

**Why SQLite?**

SQLite was chosen because:

- lightweight
- persistent
- simple setup
- ideal for structured fact storage

**Why LangGraph?**

LangGraph provides:

- explicit state management
- deterministic agent orchestration
- workflow control
- modular agent design

**Why Structured Outputs?**

Pydantic validation ensures:

- reliable downstream logic
- consistent verdict formatting
- robust workflow execution

**🚀 Future Improvements**

Potential future enhancements:

- Semantic similarity search using vector databases
- Human review dashboard
- Multi-source verification
- Advanced confidence calibration
- Real-time news ingestion pipeline
- Semantic contradiction detection

**📄 License**

This project is intended for educational and research purposes.

**👨‍💻 Author**

Developed as part of the **Sentinels of Truth** Multi-Agent Verification System project.

```mermaid
graph TD
    %% Define Styles
    classDef frontend fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    classDef engine fill:#fff3e0,stroke:#f57c00,stroke-width:2px;
    classDef agent fill:#e8f5e9,stroke:#388e3c,stroke-width:2px;
    classDef data fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px;
    classDef tool fill:#eceff1,stroke:#607d8b,stroke-width:2px,stroke-dasharray: 5 5;
    classDef decision fill:#ffebee,stroke:#d32f2f,stroke-width:2px;
    classDef insert fill:#c8e6c9,stroke:#2e7d32,stroke-width:2px;
    classDef flag fill:#ffcc80,stroke:#ef6c00,stroke-width:2px;
    classDef discard fill:#cfd8dc,stroke:#455a64,stroke-width:2px;

    %% Nodes and Flow
    A([User Input: Claim submitted]) --> B
    
    B[STREAMLIT FRONTEND <br/> • Text Input <br/> • Verify Button <br/> • Result Display]:::frontend
    B --> C
    
    C{LANGGRAPH ENGINE <br/> Orchestrates Shared State}:::engine
    C --> D
    
    subgraph Scout
        D[AGENT ALPHA <br/> • Investigates claim <br/> • Estimates confidence]:::agent
        E((DuckDuckGo <br/> Search Tool)):::tool
        D -. Searches .-> E
        E -. Retrieves .-> D
    end
    
    D --> F
    
    F[/STRUCTURED VERIFICATION REPORT <br/> • Verdict <br/> • Reasoning <br/> • Confidence/]::data
    F --> G
    
    subgraph Archivist
        G[AGENT BETA <br/> • Checks duplicates <br/> • Detects contradictions]:::agent
        H[(SQLite Database <br/> • Claims • Verdicts <br/> • Status • Timestamp)]:::data
        G -. Queries & Updates .-> H
    end
    
    G --> I{FINAL DECISION}:::decision
    
    I -->|New Verified Claim| J([INSERTED]):::insert
    I -->|Duplicate Detected| K([DISCARDED]):::discard
    I -->|Contradictory Claim| L([FLAGGED]):::flag
