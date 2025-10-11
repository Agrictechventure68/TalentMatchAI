TalentMatchAI 🎯

Revolutionizing hiring with AI fairness, speed, and transparency.

AI-Powered Fair Hiring Platform for SMEs, Corporates, and Government Agencies


---

🚀 WHY TALENT MATCH I MATTERS 

Traditional hiring is costly, biased, and time-consuming.

SMEs often lack HR capacity to screen hundreds of applicants.

Governments require transparent, accountable recruitment.

Corporates must maintain diversity, inclusion, and efficiency.


👉 TalentMatchAI transforms this process by automating fair, explainable, and data-driven applicant ranking.


---

💡 Core Value Proposition

📂 Automated CV Parsing – Extracts data from PDF/DOCX instantly.

⚖ Fairness-Driven Scoring – Every applicant gets objective, explainable rankings.

🤝 Transparency for Trust – Each score includes reasons and weights.

📊 Data-Driven Insights – Improves hiring outcomes & retention rates.


> 🧠 TalentMatchAI is beyond a hackathon project — it’s designed for real HR and government adoption.




---

✨ KEY FEATURES 

Backend (FastAPI)

RESTful API for applicant uploads, parsing, and ranking.

Machine learning scoring model using scikit-learn and pandas.

JSON output with detailed reasoning for every rank.

Modular structure for easy scaling into HR or government systems.


Frontend (HTML / CSS / JavaScript)

Clean, responsive interface for HR teams and SMEs.

Input form for applicant data (skills, education, experience).

Displays ranked results instantly with reasons.

Connects directly to the FastAPI backend.



---

🧱 FULL PROJECT STRUCTURE 

TalentMatchAI/
├── backend/
│   ├── app/
│   │   ├── main.py             # FastAPI entry point
│   │   ├── models/             # Applicant data models
│   │   ├── routers/            # Upload & ranking endpoints
│   │   ├── services/           # Parsing & scoring logic
│   │   └── utils/              # Helper scoring functions
│   ├── datasets/
│   │   └── applicants.json     # Sample dataset for testing
│   ├── requirements.txt        # Backend dependencies
│   └── README.md
│
├── frontend/
│   ├── index.html              # Main user interface
│   ├── style.css               # Styling and responsiveness
│   ├── script.js               # API integration and interactivity
│
├── docs/
│   └── pitch-deck-outline.md   # For investors, agencies, and partners
│
├── LICENSE
└── .gitignore


---

⚙️ Backend Setup Instructions

1. Clone the repository

git clone https://github.com/Agrictechventure68/TalentMatchAI.git
cd TalentMatchAI/backend


2. Create and activate virtual environment

python -m venv venv
venv\Scripts\activate       # On Windows
source venv/bin/activate    # On Mac/Linux


3. Install dependencies

pip install -r requirements.txt


4. Run the backend server

uvicorn app.main:app --reload

✅ Server Live At: http://127.0.0.1:8000

---

📡 API ENDPOINTS 

Method	Endpoint	Description

POST	/upload/	Upload applicant CV (PDF/DOCX)
GET	/rank/	Retrieve ranked applicant list


Example Response:

[
  {
    "name": "John Ade",
    "score": 87,
    "reasons": ["5 years experience", "Python & SQL skills"]
  },
  {
    "name": "Victoria Ifijeh",
    "score": 72,
    "reasons": ["Strong education", "Limited direct experience"]
  }
]

🧩 Fairness Guarantee

No hidden algorithmic weights.

All reasoning and scoring criteria are visible.

Configurable scoring ensures fairness across gender, background, and academic pedigree.

---

🌐 Frontend (Demo Interface)

1️⃣ Open the Frontend

Go to the frontend/ folder

Open index.html in your browser (or use VS Code Live Server)


2️⃣ Add Applicants

Enter multiple applicants with:

Name

Skills (comma separated)

Education

Years of Experience


3️⃣ RANK APPLICANTS 

Click “Rank Applicants” → The page calls your backend API and displays ranked results with fairness reasoning.

Example Screenshot (Frontend View):

Name	Score	Reason

Alice	95	Excellent skills, strong experience
John	89	Balanced background
Mary	78	Moderate experience


> This interface can connect to a local FastAPI backend or a deployed Render/Cloud backend at
https://talentmatchai.onrender.com/rank-applicants

---

💼 IMPACT FOR ORGANIZATIONS 

Stakeholder	Benefit

SMEs	Save up to 70% HR screening time
Corporates	Reduce hiring bias & increase retention
Government Agencies	Achieve transparency and public trust

---

🔮 FUTURE ROADMAP 

🗂 NLP-powered CV parsing (with spaCy or Transformers)

🎯 Job-role–specific ranking models

📊 Admin dashboards for HR visualization

🌍 API deployment on Render / AWS / GCP

🤖 AI-driven interview question generator



---

👤 AUTHOR 

Bright Doro (Agrictechventure68)
Educator | Agricultural & Tech Consultant | Software Developer

> Mission: Build fair, efficient, and impactful tech for Africa’s growth.



🌐 GitHub: Agrictechventure68
📧 agriempower4dcentury@gmail.com


---

📜 LICENSE 

This project is licensed under the MIT License — free to use, modify, and distribute with credit.