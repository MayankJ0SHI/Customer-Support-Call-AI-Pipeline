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
  - [CLI Pipeline](#cli-pipeline)
  - [FastAPI Server](#fastapi-server)
- [API Endpoints](#api-endpoints)
- [Docker Deployment](#docker-deployment)
- [AWS Deployment](#aws-deployment)
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
- **REST API Interface**: FastAPI-based API for programmatic access and integration
- **CORS Support**: Configured for cross-origin requests
- **Docker Ready**: Full containerization support for easy deployment

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
├── main.py                          # CLI entry point - orchestrates the entire pipeline
├── app.py                           # FastAPI entry point - REST API server
├── template.py                      # Template/example file
├── dockerfile                       # Docker container configuration
├── .dockerignore                    # Docker build ignore file
├── requirements.txt                 # Project dependencies
├── README.md                        # This file
│
├── config/
│   └── config.json                 # Configuration file (LLM settings, evaluation criteria)
│
├── data/                           # Data directory (auto-created by API)
│   ├── transcripts.xlsx            # Input data - customer call transcripts
│   └── output_*.xlsx               # Output files - analyzed and evaluated transcripts
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
│   │   ├── aggregation.py          # Results aggregation
│   │   └── inference.py            # Run full pipeline inference
│   │
│   ├── pipeline/                   # Pipeline orchestration
│   │   ├── __init__.py
│   │   ├── pipeline.py             # Main pipeline execution logic
│   │   └── inference.py            # Inference wrapper for API
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

### CLI Pipeline

Run the command-line pipeline for batch processing:

```bash
python main.py
```

#### Expected Output

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

### FastAPI Server

Run the REST API server for real-time evaluation:

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

#### Interactive API Documentation

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

---

## � API Endpoints

### Health Check

**GET** `/`

Verify that the API server is running.

**Response:**
```json
{
  "message": "QA Evaluator API is running..."
}
```

### Evaluate File

**POST** `/evaluate-file`

Upload a CSV or Excel file containing call transcripts and receive evaluated results.

**Request:**
- **Content-Type**: `multipart/form-data`
- **Parameter**: `file` (required) - CSV or XLSX file
  - Supported formats: `.csv`, `.xlsx`
  - Max file size: Limited by server configuration

**Response:**
- **Content-Type**: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- **Content**: Excel file with evaluation results

**Example using cURL:**
```bash
curl -X POST "http://localhost:8000/evaluate-file" \
  -F "file=@data/transcripts.xlsx" \
  --output results.xlsx
```

**Example using Python:**
```python
import requests

with open('data/transcripts.xlsx', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/evaluate-file',
        files={'file': f}
    )
    
with open('results.xlsx', 'wb') as output:
    output.write(response.content)
```

**Example using JavaScript:**
```javascript
const formData = new FormData();
const fileInput = document.querySelector('input[type="file"]');
formData.append('file', fileInput.files[0]);

fetch('http://localhost:8000/evaluate-file', {
  method: 'POST',
  body: formData
})
.then(response => response.blob())
.then(blob => {
  const url = window.URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'results.xlsx';
  a.click();
});
```

**Error Responses:**
```json
{
  "error": "Please upload a csv or xlsx file."
}
```

---

## 🐳 Docker Deployment

### Prerequisites

- Docker installed on your system
- Docker Compose (optional, for orchestration)

### Quick Start with Docker

#### 1. Build the Docker Image

```bash
docker build -t customer-support-qa-evaluator:latest .
```

#### 2. Run the Container

```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_key_here \
  -e GOOGLE_API_KEY=your_key_here \
  -v $(pwd)/data:/app/data \
  customer-support-qa-evaluator:latest
```

#### 3. Access the API

Once the container is running:
- **API**: `http://localhost:8000`
- **Docs**: `http://localhost:8000/docs`

### Docker Configuration Details

#### Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create data directory
RUN mkdir -p /app/data

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Expose port
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

#### .dockerignore

```
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.git
.vscode
logs/
data/
myenv/
```

### Environment Variables

When running Docker, pass environment variables using `-e` flag:

```bash
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=sk-... \
  -e GOOGLE_API_KEY=... \
  customer-support-qa-evaluator:latest
```

### Volumes

Mount the data directory to persist input/output files:

```bash
docker run -p 8000:8000 \
  -v /path/to/local/data:/app/data \
  customer-support-qa-evaluator:latest
```

### Docker Compose (Optional)

Create a `docker-compose.yml` file for easier management:

```yaml
version: '3.8'

services:
  qa-evaluator:
    build: .
    ports:
      - "8000:8000"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---
## ☁️ AWS Deployment

Deploy the QA Evaluator API on AWS using **ECS Fargate**, **ECR**, and **Application Load Balancer** for production-grade infrastructure.

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Internet Users                           │
└────────────────────┬────────────────────────────────────────┘
                     │ HTTPS/HTTP
                     ↓
    ┌─────────────────────────────────────────┐
    │  Application Load Balancer (ALB)        │
    │  qa-evaluator-alb                       │
    │  DNS: qa-evaluator-alb-xxx.amazonaws.com│
    └────────────┬────────────────────────────┘
                 │ Port 80/443
                 ↓
    ┌─────────────────────────────────────────┐
    │  Target Group                           │
    │  qa-evaluator-target-group              │
    │  Health Checks on /                     │
    └────────────┬────────────────────────────┘
                 │ Port 8000
                 ↓
    ┌─────────────────────────────────────────┐
    │  ECS Cluster (Fargate)                  │
    │  qa-evaluator-cluster                   │
    │                                         │
    │  ┌────────────────────────────────────┐ │
    │  │  ECS Task (Running Container)      │ │
    │  │  - Task Def: AI-qa-evaluator-task  │ │
    │  │  - Service: qa-evaluator-service   │ │
    │  │                                    │ │
    │  │  ┌──────────────────────────────┐  │ │
    │  │  │  Docker Container            │  │ │
    │  │  │  - Image from ECR            │  │ │
    │  │  │  - FastAPI on port 8000      │  │ │
    │  │  │  - Auto-restart on failure   │  │ │
    │  │  └──────────────────────────────┘  │ │
    │  └────────────────────────────────────┘ │
    └─────────────────────────────────────────┘
         ↕
    ┌─────────────────────────────────────────┐
    │  ECR (Elastic Container Registry)       │
    │  Stores Docker Images                   │
    └─────────────────────────────────────────┘
```

### Prerequisites

- AWS Account with credentials
- AWS CLI installed
- Docker installed locally
- IAM permissions for ECR, ECS, EC2, and IAM services

### Phase 1: AWS Authentication & Setup

**Step 1: Create IAM User for Deployment**

1. Go to AWS IAM Console
2. Create new user: `ecs-deployment-user`
3. Attach policy: `AdministratorAccess`
4. Generate Access Key and save credentials

**Step 2: Configure AWS CLI**

```bash
# Install AWS CLI
# https://aws.amazon.com/cli/

# Verify installation
aws --version

# Configure credentials
aws configure
# Enter: AWS Access Key ID, Secret Access Key, Region (us-east-1), Output format (json)

# Validate authentication
aws sts get-caller-identity
```

### Phase 2: Docker Image to ECR

**Step 3: Build and Test Locally**

```bash
# Test API locally
uvicorn app:app --host 0.0.0.0 --port 8000

# In another terminal, build Docker image
docker build -t qa-evaluator-app .

# Verify image
docker images

# Test container
docker run -p 8000:8000 --env-file .env qa-evaluator-app
```

**Step 4: Create ECR Repository**

```bash
# Go to AWS ECR Console → Create Repository
# Repository name: qa-evaluator-app
# Save the ECR URI: <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/qa-evaluator-app
```

**Step 5: Push Docker Image to ECR**

```bash
# Authenticate Docker with ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <YOUR_ECR_URI>

# Tag image for ECR
docker tag qa-evaluator-app:latest <YOUR_ECR_URI>:latest

# Push to ECR
docker push <YOUR_ECR_URI>:latest
```

### Phase 3: ECS Infrastructure

**Step 6: Create IAM Service-Linked Role**

```bash
aws iam create-service-linked-role --aws-service-name ecs.amazonaws.com
```

**Step 7: Create ECS Cluster**

1. Go to AWS ECS Console → Clusters → Create Cluster
2. Cluster name: `qa-evaluator-cluster`
3. Infrastructure: AWS Fargate (serverless)
4. Create

**Step 8: Create Task Definition**

1. Go to ECS Console → Task Definitions → Create New Task Definition
2. Configuration:
   - Family: `AI-qa-evaluator-task`
   - Launch Type: AWS Fargate
   - OS: Linux/X86_64
   - CPU: 0.5 vCPU
   - Memory: 1 GB
   - Task Execution Role: ecsTaskExecutionRole

3. Container Configuration:
   - Name: `qa-evaluator-container`
   - Image URI: `<YOUR_ECR_URI>:latest`
   - Container Port: 8000
   - Protocol: TCP

4. Create

**Step 9: Create ECS Service**

1. Open Cluster → Create Service
2. Configuration:
   - Launch Type: Fargate
   - Task Definition Family: `AI-qa-evaluator-task`
   - Service Name: `qa-evaluator-service`
   - Desired Count: 1

3. Network Configuration:
   - VPC: Default
   - Security Group: Create new with port 8000 open (0.0.0.0/0)

4. Public IP: Enable
5. Create

**Step 10: Verify Task is Running**

```bash
# Go to ECS Cluster → Services → qa-evaluator-service → Tasks
# Wait for Status = RUNNING
# Copy Public IP and visit: http://PUBLIC_IP:8000/docs
```

### Phase 4: Production Load Balancer (Optional but Recommended)

**Step 11: Create Target Group**

1. EC2 Console → Load Balancing → Target Groups → Create Target Group
2. Configuration:
   - Target Type: IP addresses
   - Name: `qa-evaluator-target-group`
   - Protocol: HTTP
   - Port: 8000
   - VPC: Default
   - Health Check Path: `/`

3. Create

**Step 12: Create Application Load Balancer**

1. EC2 Console → Load Balancers → Create Load Balancer
2. Choose: Application Load Balancer
3. Configuration:
   - Name: `qa-evaluator-alb`
   - Scheme: Internet-facing
   - Subnets: Select all available

4. Security Group: Create new with HTTP:80 (0.0.0.0/0)
5. Listener: HTTP:80 → Target Group: `qa-evaluator-target-group`
6. Create

**Step 13: Attach Load Balancer to ECS Service**

1. ECS Console → Service → `qa-evaluator-service` → Update
2. Load Balancing → Enable → Application Load Balancer
3. Select Load Balancer: `qa-evaluator-alb`
4. Container: `qa-evaluator-container:8000`
5. Target Group: `qa-evaluator-target-group`
6. Update Service

**Step 14: Test Load Balancer Endpoint**

```bash
# After 2-5 minutes (deployment time):
# EC2 Console → Load Balancers → Copy DNS name
# Visit: http://YOUR_ALB_DNS_NAME/docs
```

### Management Commands

```bash
# View service logs
# ECS Console → Cluster → Service → Tasks → Click Task → Logs

# Scale services
aws ecs update-service --cluster qa-evaluator-cluster --service qa-evaluator-service --desired-count 3

# Update application (new image)
docker build -t qa-evaluator-app .
docker tag qa-evaluator-app:latest <YOUR_ECR_URI>:latest
docker push <YOUR_ECR_URI>:latest
aws ecs update-service --cluster qa-evaluator-cluster --service qa-evaluator-service --force-new-deployment

# Delete resources
aws ecs delete-service --cluster qa-evaluator-cluster --service qa-evaluator-service --force
aws ecs delete-cluster --cluster qa-evaluator-cluster
aws ecr delete-repository --repository-name qa-evaluator-app --force
```

### Cost Estimation

- **Fargate**: ~$0.015/hour per vCPU + ~$0.0015/hour per GB
- **ALB**: ~$16/month + data processing charges
- **ECR**: $0.10 per GB stored per month
- **Data Transfer**: $0.02 per GB (outbound)

---
## �📊 Data Format

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

### Core Dependencies

```
# LLM & AI Framework
langchain                    # LLM orchestration framework
langchain-openai             # OpenAI integration
langchain-google-genai       # Google Gemini integration
langchain-community          # Community integrations

# API Framework
fastapi                      # Modern web framework for APIs
uvicorn                      # ASGI server for FastAPI

# Environment & Utilities
python-dotenv               # Environment variable management
pydantic                    # Data validation

# Data Processing
pandas                      # Data manipulation
openpyxl                    # Excel file handling
pypdf                       # PDF processing
beautifulsoup4              # Web scraping
lxml                        # XML processing

# Vector & Search
faiss-cpu                   # Vector similarity search
sentence-transformers       # Text embedding models
chromadb                    # Vector database

# Document Processing
unstructured                # Unstructured data processing
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 🆘 Troubleshooting

### CLI Pipeline Issues

#### Issue: API Key Errors
**Solution**: Ensure `.env` file contains valid API keys for OpenAI/Google

#### Issue: File Not Found Errors
**Solution**: Verify that `data/transcripts.xlsx` exists in the data folder

#### Issue: LLM Timeout
**Solution**: Increase timeout values or use a faster model variant

#### Issue: Module Import Errors
**Solution**: Ensure all dependencies are installed with `pip install -r requirements.txt`

### API Server Issues

#### Issue: Port Already in Use
**Solution**: Use a different port: `uvicorn app:app --port 8001`

#### Issue: CORS Errors in Browser
**Solution**: CORS is enabled for all origins (`allow_origins=["*"]`). Check browser console for other errors.

#### Issue: File Upload Fails
**Solution**: 
- Verify the file is in CSV or XLSX format
- Check that the `data/` directory exists and has write permissions
- Ensure file size doesn't exceed server limits

#### Issue: 422 Unprocessable Entity
**Solution**: Verify the request format is correct and file parameter is named `file`

### Docker Issues

#### Issue: Docker Build Fails
**Solution**: Ensure Docker is installed and running, and you have internet connectivity for downloading base images

#### Issue: Container Can't Access Data
**Solution**: Verify volume mount path is correct: `-v /local/path:/app/data`

#### Issue: Environment Variables Not Set
**Solution**: Pass them explicitly with `-e` flags or use a `.env` file with Docker Compose

---

## 📞 Support

For issues, questions, or suggestions, please open an issue in the repository.

---

**Last Updated**: May 26, 2026
