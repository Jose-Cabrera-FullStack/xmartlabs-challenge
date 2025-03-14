from unittest.mock import patch

import pytest

from app.infrastructure.s3 import generate_presigned_url


def test_generate_presigned_url():
    with patch("app.infrastructure.s3.boto3.client") as mock_boto3_client:
        mock_boto3_client.return_value.generate_presigned_post.return_value = {
            "url": "mocked_url",
            "fields": {"key": "mocked_key"},
        }

        response = generate_presigned_url(
            bucket_name="test_bucket",
            key="test.jpg",
            content_type="image/jpeg",
            file_size=1024,
            region="us-east-1",
        )

        assert response == {"url": "mocked_url", "fields": {"key": "mocked_key"}}
        mock_boto3_client.assert_called_once_with("s3", region_name="us-east-1")
        mock_boto3_client.return_value.generate_presigned_post.assert_called_once_with(
            "test_bucket",
            "test.jpg",
            Fields={"Content-Type": "image/jpeg"},
            Conditions=[
                {"Content-Type": "image/jpeg"},
                ["content-length-range", 0, 1024],
            ],
            ExpiresIn=3600,
        )


def test_generate_presigned_url_exception():
    with patch("app.infrastructure.s3.boto3.client") as mock_boto3_client:
        mock_boto3_client.return_value.generate_presigned_post.side_effect = Exception("Simulated S3 exception")
        with pytest.raises(Exception, match="Simulated S3 exception"):
            generate_presigned_url(
                bucket_name="test_bucket",
                key="test.jpg",
                content_type="image/jpeg",
                file_size=1024,
                region="us-east-1",
            )
