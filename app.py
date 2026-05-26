import os
import uuid
import pandas as pd

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

from src.pipeline.inference import run_full_pipeline
from src.utils.helpers import save_dataframe

app = FastAPI(
    title="Customer Support QA Evaluator",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Endpoints
@app.get("/")
def health_check():
    return {"message": "QA Evaluator API is running..."}

@app.post("/evaluate-file")
async def evaluate_file(file: UploadFile = File(...)):
    # Validation file typer
    allowed_extension = [".csv", ".xlsx"]
    
    file_extension = os.path.splitext(file.filename)[1].lower()
    
    if file_extension not in allowed_extension:
        return {
            "error": "Please upload a csv or xlsx file."
        }
    
    # Create temporary paths
    input_path = f"data/{uuid.uuid4()}{file_extension}"
    output_path = f"data/output_{uuid.uuid4()}.xlsx"
    
    # Save uploaded file
    with open(input_path, 'wb') as f:
        content = await file.read()
        f.write(content)
        
    # Load dataframe
    if file_extension == ".csv":
        df = pd.read_csv(input_path)
    elif file_extension == ".xlsx":
        df = pd.read_excel(input_path)
    
    # Run pipeline
    output_df = run_full_pipeline(df)
    
    # Save Output
    save_dataframe(output_df, output_path)
    
    # Return Output file to the user
    return FileResponse(
        path = output_path,
        filename = "qa_output.xlsx",
        media_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )