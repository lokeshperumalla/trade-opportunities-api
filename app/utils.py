from fastapi import HTTPException

ALLOWED_SECTORS = [
    "pharmaceuticals",
    "technology",
    "agriculture",
    "banking",
    "energy"
]

def validate_sector(sector: str):

    if sector.lower() not in ALLOWED_SECTORS:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sector. Allowed sectors: {ALLOWED_SECTORS}"
        )