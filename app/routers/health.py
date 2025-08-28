# Health Check 

from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "Sua app está: healthy"}

