from unittest.mock import patch, MagicMock

import pytest

from app.infrastructure.s3 import generate_presigned_url


def test_generate_presigned_url():
    # Mock the get_s3_client function instead of boto3.client directly
    with patch("app.infrastructure.s3.get_s3_client") as mock_get_s3_client:
        # Setup the mock client
        mock_s3_client = MagicMock()
        mock_get_s3_client.return_value = mock_s3_client
        
        # Setup the expected response
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

        # Call the function
        response = generate_presigned_url(
            "test-bucket", "test-key", "image/jpeg", 1024, "us-east-1"
        )

        # Verify the response
        assert response == expected_response
        
        # Verify the client was created with the correct parameters
        mock_get_s3_client.assert_called_once_with(region_name="us-east-1")
        
        # Verify generate_presigned_post was called with the correct parameters
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
    # Mock the get_s3_client function
    with patch("app.infrastructure.s3.get_s3_client") as mock_get_s3_client:
        # Setup the mock client to raise an exception
        mock_s3_client = MagicMock()
        mock_get_s3_client.return_value = mock_s3_client
        mock_s3_client.generate_presigned_post.side_effect = Exception("Test error")

        # Verify that the exception is re-raised
        with pytest.raises(Exception) as excinfo:
            generate_presigned_url(
                "test-bucket", "test-key", "image/jpeg", 1024, "us-east-1"
            )
        
        assert str(excinfo.value) == "Test error"
        
        # Verify the client was created
        mock_get_s3_client.assert_called_once_with(region_name="us-east-1")
