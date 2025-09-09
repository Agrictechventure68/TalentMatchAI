from fastapi import APIRouter, UploadFile, File
from app.services.parser import parse_cv

router = APIRouter(tags=["Upload"])

@router.post("/upload")
async def upload_applicant(file: UploadFile = File(...)):
    # For demo, save file temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(await file.read())

    parsed_data = parse_cv(file_location)

    return {
        "filename": file.filename,
        "parsed_data": parsed_data
    }