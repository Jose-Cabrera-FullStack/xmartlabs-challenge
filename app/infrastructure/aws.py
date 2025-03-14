from typing import Optional, Any

import boto3

from app.settings import settings


class AWSClientFactory:
    """Factory for AWS client creation with proper configuration."""

    @staticmethod
    def get_client(
        service_name: str,
        region_name: Optional[str] = None,
        endpoint_url: Optional[str] = None,
        **kwargs: Any
    ):
        """
        Create an AWS client for the specified service with proper configuration.

        Args:
            service_name: AWS service name (e.g., 's3', 'sqs', etc.)
            region_name: AWS region name, defaults to settings.s3_region for S3
            endpoint_url: Custom endpoint URL (e.g., for local development with MinIO)
            **kwargs: Additional arguments to pass to boto3.client

        Returns:
            AWS service client
        """
        if region_name is None:
            if service_name == 's3':
                region_name = settings.s3_region
            else:
                region_name = 'us-east-1'

        if endpoint_url is None and hasattr(settings, 'aws_s3_endpoint_url'):
            if service_name == 's3' and settings.aws_s3_endpoint_url:
                endpoint_url = settings.aws_s3_endpoint_url

        return boto3.client(
            service_name,
            region_name=region_name,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=endpoint_url,
            **kwargs
        )


def get_s3_client(region_name=None):
    """
    Get an S3 client with proper configuration.

    Args:
        region_name: AWS region name, defaults to settings.s3_region

    Returns:
        S3 client
    """
    return AWSClientFactory.get_client('s3', region_name=region_name)
