from fastapi import FastAPI, UploadFile, File
import pandas as pd
from utils import check_labels

app = FastAPI(title="DataBridge Quality Checker")

@app.post("/analyze-csv/")
async def analyze_csv(file: UploadFile = File(...), gold_file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    gold = pd.read_csv(gold_file.file)
    
    accuracy, mistakes = check_labels(df, gold)
    
    return {
        "accuracy": f"{accuracy:.2f}%",
        "mistakes_count": len(mistakes),
        "mistakes_preview": mistakes.head(5).to_dict(orient="records")
    }

