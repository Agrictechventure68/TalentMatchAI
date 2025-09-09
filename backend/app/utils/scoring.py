def score_applicant(applicant: dict) -> float:
    """
    Dummy scoring function.
    Later, will implement weighted ranking by skills, experience, etc.
    """
    return len(applicant.get("skills", [])) * 10