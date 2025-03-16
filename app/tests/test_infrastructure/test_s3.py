from unittest.mock import patch, MagicMock

import pytest

from app.infrastructure.s3 import generate_presigned_url


def test_generate_presigned_url():
    with patch("app.infrastructure.s3.get_s3_client") as mock_get_s3_client:
        mock_s3_client = MagicMock()
        mock_get_s3_client.return_value = mock_s3_client

        expected_response = {
            "url": "https://test-bucket.s3.amazonaws.com/",
            "fields": {
                "key": "test-key",
                "AWSAccessKeyId": "test-access-key",
                "policy": "test-policy",
                "signature": "test-signature",
            },
        }
        mock_s3_client.generate_presigned_post.return_value = expected_response

        response = generate_presigned_url(
            "test-bucket", "test-key", "image/jpeg", 1024, "us-east-1"
        )

        assert response == expected_response

        mock_get_s3_client.assert_called_once_with(region_name="us-east-1")

        mock_s3_client.generate_presigned_post.assert_called_once_with(
            "test-bucket",
            "test-key",
            Fields={"Content-Type": "image/jpeg"},
            Conditions=[
                {"Content-Type": "image/jpeg"},
                ["content-length-range", 0, 1024],
            ],
            ExpiresIn=3600,
        )


def test_generate_presigned_url_exception():
    with patch("app.infrastructure.s3.get_s3_client") as mock_get_s3_client:
        mock_s3_client = MagicMock()
        mock_get_s3_client.return_value = mock_s3_client
        mock_s3_client.generate_presigned_post.side_effect = Exception("Test error")

        with pytest.raises(Exception) as excinfo:
            generate_presigned_url(
                "test-bucket", "test-key", "image/jpeg", 1024, "us-east-1"
            )

        assert str(excinfo.value) == "Test error"

        mock_get_s3_client.assert_called_once_with(region_name="us-east-1")

