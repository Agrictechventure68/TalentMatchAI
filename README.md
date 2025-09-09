# TalentMatchAI 🎯

AI-driven Applicant Selection & Ranking System — built for *PLP & LSETF Hackathon*.  
Designed to solve *HRTech + EdTech* challenges by enabling fair, fast, and scalable applicant evaluation.

---

## 🚀 Problem
LSETF/PLP receives thousands of applications. Manual review is:
- Slow
- Prone to bias
- Resource intensive

---

## 💡 Solution
*TalentMatchAI* uses *AI + NLP* to:
1. Parse CVs, cover letters, and assessments
2. Match against program criteria
3. Score & rank applicants
4. Provide dashboards with recommendations
5. Integrate with LMS & SME systems

---

## 🛠 Tech Stack
- *Backend:* Python (FastAPI, Uvicorn)
- *AI/NLP:* spaCy, Hugging Face Transformers
- *Database:* PostgreSQL / SQLite
- *Frontend:* React + TailwindCSS
- *Integration:* REST API

---
## 📂 Project Structure

TalentMatchAI/ │── backend/        # FastAPI app (main.py, routers, services) │── datasets/       # Applicant data & mock resumes │── docs/           # Pitch deck, requirements, diagrams │── frontend/       # React dashboard │── .gitignore      # Git ignore rules │── README.md       # Project documentation

---

## ⚡ Quick Start

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
uvicorn main:app --reload

Frontend

cd frontend
npm install
npm start


---
🎥 Deliverables

Prototype system (upload → parse → rank → dashboard)

Documentation & pitch deck

Demo video for hackathon

---
🌍 Future Vision

Beyond LSETF/PLP, the system can:

Power SME recruitment

Support EdTech admissions

Enable fair hiring processes in Nigeria & beyond