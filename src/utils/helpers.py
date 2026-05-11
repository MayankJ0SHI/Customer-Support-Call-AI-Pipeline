import pandas as pd

def save_dataframe(df, file_path: str = "data/output.xlsx"):
    df.to_excel(file_path, index=False)