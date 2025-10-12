from fastapi import FastAPI, UploadFile, File
from typing import List
import json
import os

# Import improved scoring logic
from app.services.scoring import score_applicant_advanced

app = FastAPI(title="TalentMatchAI - Applicant Ranking API")

# -----------------------------
# Load Applicants Dataset
# -----------------------------
DATASET_PATH = os.path.join(os.path.dirname(__file__), "../datasets/applicants.json")

def load_applicants():
    """Load applicants data from JSON file."""
    with open(DATASET_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

# -----------------------------
# Simple Scoring Logic (Built-in)
# -----------------------------
def score_applicant(applicant):
    """Basic scoring logic for quick tests."""
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

# -----------------------------
# Routes
# -----------------------------
@app.get("/")
def home():
    return {"message": "Welcome to TalentMatchAI - Applicant Ranking API"}

@app.get("/rank-applicants")
def rank_applicants():
    """
    Basic scoring route using in-file logic.
    """
    applicants = load_applicants()
    ranked = [score_applicant(a) for a in applicants]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

@app.get("/score-applicants")
def score_applicants():
    """
    Advanced scoring route using external scoring.py logic.
    """
    applicants = load_applicants()
    ranked = [score_applicant_advanced(a) for a in applicants]
    ranked.sort(key=lambda x: x["score"], reverse=True)
    return ranked

@app.post("/upload-cv")
async def upload_cv(file: UploadFile = File(...)):
    """
    Upload applicant CV (PDF/DOCX) - placeholder for future parsing.
    """
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)
    file_location = os.path.join(upload_dir, file.filename)

    with open(file_location, "wb") as f:
        f.write(await file.read())

    return {"message": f"Uploaded {file.filename} successfully"}