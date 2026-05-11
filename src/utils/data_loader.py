import pandas as pd
import os

def load_transcript(file_path = "data/transcripts.xlsx"):
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{os.path.basename(file_path)} file does not exist at the location: {file_path}")
    
    transcript_df = pd.read_excel(file_path)
    return transcript_df