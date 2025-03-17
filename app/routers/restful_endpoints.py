from fastapi import APIRouter, HTTPException

from app.service.presigned_url import PresignedURLService
from app.service.file_storage import FileStorageService
from app.schemas.request import PresignedURLRequest, UpdateFileStatusRequest
from app.schemas.response.update_file_status_response import UpdateFileStatusResponse
from app.schemas.response.presigned_url_response import PresignedURLResponse

router = APIRouter()


@router.post("/presigned-url", response_model=PresignedURLResponse)
async def create_presigned_url(request: PresignedURLRequest) -> PresignedURLResponse:
    """
    Create a presigned URL for uploading a file to S3.
    Receives filename, type, and file size.
    Returns the URL, file key (UUID), and status.
    """
    try:
        response = await PresignedURLService.create_presigned_url(
            request.filename, request.type, request.file_size
        )
        return PresignedURLResponse(**response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/file-status")
async def update_file_status(request: UpdateFileStatusRequest) -> UpdateFileStatusResponse:
    """
    Update the status of a file after it has been uploaded.
    Receives the file's UUID and the new status.
    """
    try:
        file = await FileStorageService.update_file_status(
            request.uuid, request.status
        )
        if not file:
            raise HTTPException(status_code=404, detail="File not found")

        return UpdateFileStatusResponse.from_orm(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
