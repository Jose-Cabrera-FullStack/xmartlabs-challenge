from app.infrastructure.s3 import generate_presigned_url
from app.settings import settings
from app.repository.file_storage_repository import FileStorageRepository


class PresignedURLService:
    """
    A service class to generate presigned URLs for S3 uploads.
    """

    @staticmethod
    async def create_presigned_url(filename: str, type: str, file_size: int) -> dict:
        """
        Create a presigned URL for uploading a file to S3 and record in database.
        """
        content_type_mapping = {
            "image": "image/jpeg",
            "video": "video/mp4"
        }

        content_type = content_type_mapping.get(type)

        try:
            file_storage = await FileStorageRepository.create_file(
                name=filename,
                type=type,
                size=file_size
            )

            presigned_response = generate_presigned_url(
                bucket_name=settings.s3_bucket_name,
                key=filename,
                content_type=content_type or "",
                file_size=file_size,
                region=settings.s3_region,
            )

            return {
                "url": presigned_response["url"],
                "key": file_storage.uuid,
                "status": file_storage.status
            }
        except Exception as e:
            raise e
