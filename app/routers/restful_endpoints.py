from fastapi import APIRouter, HTTPException
from ormar import NoMatch
from app.service.presigned_url import PresignedURLService
from app.schemas.request import PresignedURLRequest

router = APIRouter()

@router.post("/presigned-url")
async def create_presigned_url(request: PresignedURLRequest) -> dict:
    """
    Create a presigned URL for uploading a file to S3.
    Receives filename, type, and file size.
    """
    try:
        response = PresignedURLService.create_presigned_url(
            request.filename, request.type, request.file_size
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
