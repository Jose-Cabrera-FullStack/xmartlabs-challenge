from typing import Dict

from app.infrastructure.aws import get_s3_client


def generate_presigned_url(
    bucket_name: str, key: str, content_type: str, file_size: int, region: str
) -> Dict[str, str]:
    """
    Generate a presigned URL for uploading a file to an S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        key (str): The key (path) where the file will be stored in the bucket.
        content_type (str): The MIME type of the file to be uploaded.
        file_size (int): The maximum size of the file to be uploaded, in bytes.
        region (str): The AWS region where the S3 bucket is located.

    Returns:
        Dict[str, str]: A dictionary containing the presigned URL and additional fields required
        for the upload.
    """
    s3_client = get_s3_client(region_name=region)
    one_hour = 3600
    try:
        response = s3_client.generate_presigned_post(
            bucket_name,
            key,
            Fields={"Content-Type": content_type},
            Conditions=[
                {"Content-Type": content_type},
                ["content-length-range", 0, file_size],
            ],
            ExpiresIn=one_hour,
        )
        return response
    except Exception as e:
        raise e
