import json
import os

# Path to dataset
DATA_FILE = os.path.join(os.path.dirname(__file__), "../../datasets/sample_applicants.json")

def load_applicants():
    """Load applicants from dataset JSON file."""
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print("Error loading applicants:", e)
        return []

def score_applicant(applicant):
    """Assign score based on skills, experience, and certifications."""
    base_score = 0
    reasons = []

    # Experience scoring (max 40 points)
    exp = applicant.get("experience_years", 0)
    exp_score = min(exp * 8, 40)  # 5 years = 40 pts
    base_score += exp_score
    reasons.append(f"{exp} years experience → +{exp_score:.0f} pts")

    # Skills scoring (max 50 points)
    skills = applicant.get("skills", [])
    skill_count = len(skills)
    skill_score = min(skill_count * 10, 50)  # 5+ skills = 50 pts
    base_score += skill_score
    reasons.append(f"{skill_count} relevant skills → +{skill_score:.0f} pts")

    # Certifications bonus (max 10 points)
    certs = applicant.get("certifications", [])
    cert_score = min(len(certs) * 5, 10)
    base_score += cert_score
    if certs:
        reasons.append(f"{len(certs)} certifications → +{cert_score:.0f} pts")

    # Normalize total to max 100
    total_score = min(base_score, 100)

    return total_score, reasons


def rank_applicants():
    """Return ranked applicants with scores and reasons."""
    applicants = load_applicants()
    ranked = []

    for applicant in applicants:
        score, reasons = score_applicant(applicant)
        ranked.append({
            "name": applicant.get("name", "Unknown"),
            "preferred_role": applicant.get("preferred_role", "N/A"),
            "score": score,
            "reasons": reasons
        })

    # Sort from highest to lowest
    ranked = sorted(ranked, key=lambda x: x["score"], reverse=True)
    return ranked


# Debug/Test (optional)
if __name__ == "__main__":
    for r in rank_applicants():
        print(r)