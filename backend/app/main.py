from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import os
import shutil
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ------------------------------------------------------------
# MAIN FASTAPI APP
# ------------------------------------------------------------
app = FastAPI(
    title="TalentMatchAI",
    description="AI-powered CV parsing and applicant ranking system for SMEs and agencies",
    version="1.0.0"
)

# Folder to store uploaded files
UPLOAD_DIR = "datasets/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ------------------------------------------------------------
# SAMPLE JOB DESCRIPTION (for demonstration)
# In practice, this will come from employer input or database.
# ------------------------------------------------------------
JOB_DESCRIPTION = """
We are seeking a Python Backend Developer with experience in:
- FastAPI or Django
- REST APIs
- SQL/Databases
- Team collaboration
"""

# ------------------------------------------------------------
# HELPER FUNCTION: Extract text from CV (simplified for demo)
# Later, can expand with libraries like PyMuPDF, docx2txt, etc.
# ------------------------------------------------------------
def extract_text_from_file(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


# ------------------------------------------------------------
# ENDPOINT 1: Upload CVs
# ------------------------------------------------------------
@app.post("/upload_cv/")
async def upload_cv(file: UploadFile = File(...)):
    """
    Upload applicant CVs or cover letters.
    Files are stored in datasets/uploads/ for processing.
    """
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"message": f"Uploaded {file.filename} successfully", "path": file_path}


# ------------------------------------------------------------
# ENDPOINT 2: Rank Applicants
# ------------------------------------------------------------
@app.get("/rank_applicants/")
def rank_applicants():
    """
    Reads all CVs in datasets/uploads/,
    compares them against the job description,
    ranks them fairly, and returns reasons for each score.
    """
    applicants = []
    file_list = os.listdir(UPLOAD_DIR)

    if not file_list:
        return {"message": "No applicants uploaded yet."}

    for file_name in file_list:
        file_path = os.path.join(UPLOAD_DIR, file_name)
        cv_text = extract_text_from_file(file_path)

        applicants.append({
            "name": file_name.replace(".txt", ""),
            "cv_text": cv_text
        })

    # Combine job description + applicants' CVs
    documents = [JOB_DESCRIPTION] + [a["cv_text"] for a in applicants]

    # Convert text to numerical vectors using TF-IDF
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(documents)

    # Similarity between job description (index 0) and each CV
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Assign scores back to applicants
    for i, score in enumerate(similarity_scores):
        applicants[i]["score"] = round(float(score) * 100, 2)  # percentage match
        applicants[i]["reason"] = (
            f"CV matches {applicants[i]['score']}% with required skills "
            f"(based on keywords from Python, FastAPI/Django, REST API, SQL)."
        )

    # Sort applicants by score (descending)
    ranked_applicants = sorted(applicants, key=lambda x: x["score"], reverse=True)

    return JSONResponse(content={"job_description": JOB_DESCRIPTION, "rankings": ranked_applicants})


# ------------------------------------------------------------
# ENDPOINT 3: Health Check
# ------------------------------------------------------------
@app.get("/")
def root():
    return {"message": "TalentMatchAI is running. Use /upload_cv/ to add applicants and /rank_applicants/ to evaluate."}