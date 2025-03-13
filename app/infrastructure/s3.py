from typing import Dict

import boto3

def generate_presigned_url(
    bucket_name: str, key: str, content_type: str, file_size: int, region: str
) -> Dict[str, str]:
    """
    Generate a presigned URL for uploading a file to S3.
    """
    s3_client = boto3.client("s3", region_name=region)
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
