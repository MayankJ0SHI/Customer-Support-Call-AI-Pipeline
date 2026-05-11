# Customer-Support-Call-AI-Pipeline

An intelligent AI-powered pipeline for analyzing, classifying, and evaluating customer support call transcripts. This system leverages Language Models (LLMs) to automatically classify calls, route them intelligently, and provide comprehensive evaluation reports based on multiple quality metrics.

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Workflow](#workflow)
- [Project Architecture](#project-architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Data Format](#data-format)
- [Output](#output)
- [Components](#components)
- [Requirements](#requirements)

---

## 🎯 Overview

This AI pipeline automates the analysis of customer support call transcripts by:

1. **Classifying** calls into predefined categories (billing, claims, complaint, general query)
2. **Routing** calls to specific evaluation criteria based on their type
3. **Evaluating** calls across multiple quality dimensions (tone/empathy, knowledge accuracy, resolution quality)
4. **Generating** comprehensive reports with actionable recommendations

The system uses LangChain to orchestrate LLM calls and uses Pydantic for robust data validation and structured outputs.

---

## ✨ Key Features

- **Automatic Call Classification**: Categorizes support calls into billing, claims, complaints, or general queries
- **Intelligent Routing**: Routes calls to relevant evaluation criteria based on type
- **Multi-Metric Evaluation**: Assesses calls on:
  - **Tone & Empathy** - For complaint-related calls
  - **Knowledge Accuracy** - For technical/billing/claims calls
  - **Resolution Quality** - For billing, claims, and complaint calls
- **Structured Data Processing**: Uses Pydantic models for type-safe data handling
- **Batch Processing**: Processes multiple transcripts efficiently with progress tracking
- **Flexible LLM Integration**: Supports multiple LLM providers (OpenAI, Google Gemini)
- **Excel Report Export**: Generates detailed analysis reports in Excel format

---

## 🔄 Workflow

The pipeline executes the following steps in sequence:

```
Input Transcripts (Excel)
         ↓
    [Step 1: Classification]
    Classify call types & confidence scores
         ↓
    [Step 2: Routing]
    Determine evaluation criteria per call type
         ↓
    [Step 3: Evaluation]
    Run multi-metric evaluation chains
         ↓
    [Step 4: Report Generation]
    Create summary & recommendations
         ↓
    [Step 5: Export Results]
    Save comprehensive report (Excel)
```

### Call Type Routing Rules

| Call Type | Evaluation Criteria |
|-----------|-------------------|
| **Billing** | Knowledge Accuracy, Resolution Quality |
| **Claims** | Knowledge Accuracy, Resolution Quality |
| **Complaint** | Tone & Empathy, Resolution Quality |
| **General Query** | Knowledge Accuracy |

---

## 🏗️ Project Architecture

```
Customer-Support-Call-AI-Pipeline/
│
├── main.py                          # Entry point - orchestrates the entire pipeline
├── template.py                      # Template/example file
├── requirements.txt                 # Project dependencies
├── README.md                        # This file
│
├── config/
│   └── config.json                 # Configuration file (LLM settings, evaluation criteria)
│
├── data/
│   ├── transcripts.xlsx            # Input data - customer call transcripts
│   └── output.xlsx                 # Output - analyzed and evaluated transcripts
│
├── src/
│   ├── __init__.py
│   │
│   ├── components/                 # Core processing components
│   │   ├── __init__.py
│   │   ├── classification.py       # Call type classification logic
│   │   ├── router.py               # Intelligent routing logic
│   │   ├── evaluation.py           # Evaluation chains (tone, knowledge, resolution)
│   │   ├── reporting.py            # Final report generation
│   │   └── aggregation.py          # Results aggregation
│   │
│   ├── pipeline/                   # Pipeline orchestration
│   │   ├── __init__.py
│   │   └── pipeline.py             # Main pipeline execution logic
│   │
│   └── utils/                      # Utility functions
│       ├── __init__.py
│       ├── config_loader.py        # Load configuration from JSON
│       ├── data_loader.py          # Load transcript data from Excel
│       ├── llm_loader.py           # Load and initialize LLM models
│       └── helpers.py              # Helper utilities (data saving, etc.)
│
├── myenv/                          # Python virtual environment
└── logs/                           # Log files directory
```

---

## 📦 Installation

### Prerequisites

- Python 3.9+
- pip or conda

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Customer-Support-Call-AI-Pipeline
   ```

2. **Create and activate a virtual environment**
   ```bash
   # Windows
   python -m venv myenv
   myenv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   ```

---

## ⚙️ Configuration

Edit `config/config.json` to customize the pipeline behavior:

```json
{
    "llm": {
        "openai_model": "gpt-4o-mini",
        "gemini_model": "gemini-1.5-flash",
        "temperature": 0.3
    },
    "evaluation": {
        "criteria": [
            "tone_empathy",
            "knowledge_accuracy",
            "resolution_quality"
        ],
        "score_range": [1, 5]
    },
    "classification": {
        "labels": [
            "billing",
            "claims",
            "complaint",
            "general_query"
        ]
    }
}
```

### Configuration Parameters

| Section | Parameter | Description |
|---------|-----------|-------------|
| **llm** | openai_model | OpenAI model to use (e.g., gpt-4o-mini) |
| **llm** | gemini_model | Google Gemini model to use |
| **llm** | temperature | Model temperature (0.0-1.0) for response creativity |
| **evaluation** | criteria | List of evaluation metrics to compute |
| **evaluation** | score_range | Min and max values for scores |
| **classification** | labels | Categories for call classification |

---

## 🚀 Usage

### Running the Pipeline

```bash
python main.py
```

### Expected Output

The pipeline will display progress indicators for each step:

```
===== 🔃 Loading the Config and Transcripts ======
Config and Transcripts are loaded successfully ✅

===== 🔃 Loading the LLM ======
Loaded the LLM ChatOpenAI successfully ✅

===== 👾 Creating the Chains ======
Created the chains successfully ✅

====== 🅿️ Pipeline Triggerred =====

Step 1️⃣: Running the Call Type Classification
Classification of the Calls: 100%|██████████| 5/5 [00:10<00:00,  2.00s/it]

Step 2️⃣: Routing to the respective call type for evaluation

Step 3️⃣: Performing the evaluation
Running the Evaluation: 100%|██████████| 5/5 [00:25<00:00,  5.00s/it]

Step 4️⃣: Generating the final report
Final Report Summary Generation: 100%|██████████| 5/5 [00:15<00:00,  3.00s/it]

Step 5️⃣: Saving the report

====== 🅿️ Pipeline Executed Successfully ✅✅✅ =====
```

---

## 📊 Data Format

### Input Data: `data/transcripts.xlsx`

Required columns:

| Column | Type | Description |
|--------|------|-------------|
| **call_id** | string | Unique identifier for each call |
| **transcript** | string | Full transcript of the customer support call |
| **timestamp** | datetime | When the call occurred |
| **agent_name** | string | Name of the support agent |

Example:

```
call_id  | transcript                                  | timestamp          | agent_name
---------|---------------------------------------------|--------------------|-----------
CALL001  | Customer: Hello... Agent: Hi, how can I help? | 2024-01-15 10:30  | John Smith
CALL002  | Customer: I need help with billing...       | 2024-01-15 11:00  | Jane Doe
```

---

## 📈 Output

### Output File: `data/output.xlsx`

The output Excel file contains all input columns plus:

| Column | Description |
|--------|-------------|
| **predicted_call_type** | Classified call category (billing, claims, complaint, general_query) |
| **confidence** | Confidence score (0-1) for classification |
| **evaluation_plan** | List of evaluation criteria applied |
| **evaluation_output** | Detailed evaluation results (nested JSON structure) |
| **summary** | Executive summary of the call evaluation |
| **recommendations** | Actionable recommendations based on evaluation |

### Evaluation Output Structure

```json
{
  "tone": {
    "empathy_score": 4,
    "feedback": "Agent showed good empathy...",
    "suggestions": "..."
  },
  "knowledge": {
    "accuracy_score": 5,
    "feedback": "Agent provided accurate information...",
    "suggestions": "..."
  },
  "resolution": {
    "quality_score": 4,
    "feedback": "Issue was resolved effectively...",
    "suggestions": "..."
  }
}
```

---

## 🔧 Components

### 1. **Classification** (`src/components/classification.py`)
- **Purpose**: Classify incoming calls into predefined categories
- **Output**: Call type with confidence score
- **LLM Chain**: Uses Pydantic output parser for structured results

### 2. **Router** (`src/components/router.py`)
- **Purpose**: Determine evaluation criteria based on call type
- **Logic**: Routes billing/claims to knowledge+resolution; complaints to tone+resolution; general queries to knowledge only
- **Output**: Evaluation plan per call

### 3. **Evaluation** (`src/components/evaluation.py`)
- **Purpose**: Multi-metric assessment of calls
- **Chains**:
  - **Tone Chain**: Assesses empathy and emotional support
  - **Knowledge Chain**: Verifies factual accuracy and product knowledge
  - **Resolution Chain**: Evaluates quality of problem resolution
- **Output**: Scored evaluations with feedback

### 4. **Reporting** (`src/components/reporting.py`)
- **Purpose**: Generate executive summaries and recommendations
- **Input**: Evaluation results
- **Output**: Summary text and actionable recommendations

### 5. **Pipeline Orchestration** (`src/pipeline/pipeline.py`)
- **Purpose**: Coordinate all components in sequence
- **Functions**:
  - `run_classification()`: Execute classification on all transcripts
  - `apply_evaluation()`: Run evaluation chains
  - `generate_final_report()`: Create summaries and recommendations

### 6. **Utilities** (`src/utils/`)
- **config_loader.py**: Loads configuration from JSON
- **data_loader.py**: Reads Excel transcripts
- **llm_loader.py**: Initializes LLM models
- **helpers.py**: Data export and utility functions

---

## 📋 Requirements

```
langchain                    # LLM orchestration framework
langchain-openai             # OpenAI integration
langchain-google-genai       # Google Gemini integration
langchain-community          # Community integrations
python-dotenv               # Environment variable management
pypdf                       # PDF processing
beautifulsoup4              # Web scraping
lxml                        # XML processing
unstructured                # Unstructured data processing
faiss-cpu                   # Vector similarity search
sentence-transformers       # Text embedding models
chromadb                    # Vector database
pandas                      # Data manipulation
openpyxl                    # Excel file handling
pydantic                    # Data validation
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🆘 Troubleshooting

### Issue: API Key Errors
**Solution**: Ensure `.env` file contains valid API keys for OpenAI/Google

### Issue: File Not Found Errors
**Solution**: Verify that `data/transcripts.xlsx` exists in the data folder

### Issue: LLM Timeout
**Solution**: Increase timeout values or use a faster model variant

---

## 📞 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Last Updated**: May 2024
