"""

"""
from app.infrastructure.s3 import generate_presigned_url
from app.settings import settings


class PresignedURLService:
    """
    A service class to generate presigned URLs for S3 uploads.
    """

    @staticmethod
    def create_presigned_url(filename: str, type: str, file_size: int) -> dict:
        """
        Create a presigned URL for uploading a file to S3.
        """
        content_type_mapping = {
            "image": "image/jpeg",
            "video": "video/mp4"
        }

        content_type = content_type_mapping.get(type)

        try:
            response = generate_presigned_url(
                bucket_name=settings.s3_bucket_name,
                key=filename,
                content_type=content_type,
                file_size=file_size,
                region=settings.s3_region,
            )
            return response
        except Exception as e:
            raise e
