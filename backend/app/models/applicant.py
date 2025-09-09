from pydantic import BaseModel
from typing import Optional

class Applicant(BaseModel):
    id: Optional[int]
    name: str
    email: str
    phone: str
    skills: list[str] = []
    experience: Optional[str] = None
    education: Optional[str] = None
    score: Optional[float] = None