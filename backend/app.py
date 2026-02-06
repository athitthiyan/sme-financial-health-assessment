import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from analysis import analyze_financials
from scoring import calculate_health_score
from ai_insights import generate_insights

app = FastAPI(title="SME Financial Health API")

# ✅ CORS CONFIG (THIS FIXES YOUR ERROR)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all for hackathon
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)

    analysis = analyze_financials(df)
    score = calculate_health_score(
        analysis["revenue"], analysis["expenses"]
    )

    analysis["score"] = score
    insights = generate_insights(analysis)

    return {
        "financials": analysis,
        "health_score": score,
        "ai_insights": insights
    }
