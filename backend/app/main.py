from fastapi import FastAPI, UploadFile, File
from typing import List
import json
import os

app = FastAPI(title="TalentMatchAI - Applicant Ranking System")

# Load applicants from JSON
DATASET_PATH = os.path.join(os.path.dirname(__file__), "../datasets/applicants.json")

def load_applicants():
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def score_applicant(applicant):
    """Simple scoring logic with reasons (can be improved later)."""
    score = 0
    reasons = []

    if "python" in applicant.get("skills", "").lower():
        score += 30
        reasons.append("Python skill matched")
    if "experience" in applicant and applicant["experience"] >= 5:
        score += 25
        reasons.append("5+ years of experience")
    if "certifications" in applicant and applicant["certifications"]:
        score += 20
        reasons.append("Has certifications")
    if "leadership" in applicant.get("skills", "").lower():
        score += 15
        reasons.append("Leadership skills")
    if "ai" in applicant.get("skills", "").lower():
        score += 10
        reasons.append("AI knowledge")

    return {"name": applicant["name"], "score": score, "reasons": reasons}

@app.get("/")
def home():
    return {"message": "Welcome to TalentMatchAI - Applicant Ranking API"}

@app.get("/rank-applicants")
def rank_applicants():
    applicants = load_applicants()
    ranked = [score_applicant(a) for a in applicants]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    file_location = f"uploads/{file.filename}"
    os.makedirs("uploads", exist_ok=True)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"message": f"Uploaded {file.filename} successfully"}