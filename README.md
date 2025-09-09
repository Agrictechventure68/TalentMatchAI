TalentMatchAI 🎯

AI-Powered Fair Hiring Platform for SMEs, Corporates, and Government Agencies

🚀 Why TalentMatchAI Matters

Hiring is costly, biased, and time-consuming for many organizations.

SMEs struggle with limited HR staff and resources.

Government agencies need fair, transparent recruitment to gain public trust.

Corporates must process hundreds of CVs quickly while keeping diversity & inclusion goals.


👉 TalentMatchAI solves these pain points by providing:

📂 Automated CV/Document parsing & ranking – saves hours of manual screening

⚖ Fairness-driven scoring – candidates are ranked with clear reasons behind every decision

🤝 Transparency for trust – agencies can defend their recruitment choices with evidence

📊 Data-driven insights – ensures the right fit, reduces turnover, and improves productivity


TalentMatchAI is not just a hackathon project — it’s designed for real adoption in the workplace.


---

✨ Key Features

Upload CVs, cover letters, or documents (PDF/DOCX) via browser or system file picker

Extracts key details: skills, education, experience

Ranks applicants with reasons for every score

Provides a JSON-based applicant dataset for transparency

Ready to scale into HR portals, e-government platforms, and corporate systems



---

📂 Project Structure

TalentMatchAI/
├── backend/
│   ├── app/
│   │   ├── main.py          # FastAPI entry point
│   │   ├── models/          # Applicant model
│   │   ├── routers/         # Upload endpoints
│   │   ├── services/        # Parsing & scoring logic
│   │   └── utils/           # Helper scoring functions
│   └── requirements.txt     # Dependencies
├── datasets/
│   └── applicants.json      # Sample applicants for testing
├── docs/
│   └── pitch-deck-outline.md (optional for investors/agencies)
├── README.md
└── .gitignore


---

🛠 Setup Instructions

1. Clone the repository

git clone https://github.com/Agrictechventure68/TalentMatchAI.git
cd TalentMatchAI/backend

2. Create virtual environment

python -m venv venv
venv\Scripts\activate   # on Windows

3. Install dependencies

pip install -r requirements.txt

4. Run the backend server

uvicorn app.main:app --reload

The API will be live at 👉 http://127.0.0.1:8000


---

🧪 Demo Usage

Upload Applicants’ CVs

POST request to /upload/ with a file (PDF/DOCX).

The system extracts skills, education, experience.

Adds the candidate to the dataset.


Rank Applicants

GET request to /rank/ returns:

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

Fairness Guarantee

No hidden weights — all reasons are visible.

Configurable scoring ensures fairness across gender, background, and academic pedigree.



---

📊 Impact for SMEs & Agencies

SMEs → Save up to 70% HR screening time

Corporates → Reduce hiring bias & improve retention

Government → Achieve transparent, trust-driven recruitment



---
🤝 Future Roadmap

AI-based interview question generator

Job-role specific ranking models

Integration into HRIS & e-Gov portals

Full frontend with dashboards for HR managers



---
👤 Author

Bright Doro (Agrictechventure68)

Educator | Agricultural & Tech Consultant | Software Developer

Mission: To build fair, efficient, and impactful tech for Africa’s growth