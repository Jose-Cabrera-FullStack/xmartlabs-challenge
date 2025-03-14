from unittest.mock import patch, MagicMock

from app.infrastructure.aws import AWSClientFactory, get_s3_client
from app.settings import settings


class TestAWSClientFactory:
    @patch("app.infrastructure.aws.boto3.client")
    def test_get_client_basic(self, mock_boto3_client):
        mock_client = MagicMock()
        mock_boto3_client.return_value = mock_client
        client = AWSClientFactory.get_client("dynamodb", region_name="us-west-2")
        mock_boto3_client.assert_called_once_with(
            "dynamodb",
            region_name="us-west-2",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=None,
        )
        assert client == mock_client

    @patch("app.infrastructure.aws.boto3.client")
    def test_get_client_default_region_s3(self, mock_boto3_client):
        AWSClientFactory.get_client("s3")
        mock_boto3_client.assert_called_once_with(
            "s3",
            region_name=settings.s3_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=settings.aws_s3_endpoint_url,
        )

    @patch("app.infrastructure.aws.boto3.client")
    def test_get_client_default_region_non_s3(self, mock_boto3_client):
        AWSClientFactory.get_client("sqs")
        mock_boto3_client.assert_called_once_with(
            "sqs",
            region_name="us-east-1",
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=None,
        )

    @patch("app.infrastructure.aws.boto3.client")
    def test_get_client_with_endpoint_url(self, mock_boto3_client):
        custom_endpoint = "http://custom-endpoint:1234"
        AWSClientFactory.get_client("s3", endpoint_url=custom_endpoint)
        mock_boto3_client.assert_called_once_with(
            "s3",
            region_name=settings.s3_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=custom_endpoint,
        )

    @patch("app.infrastructure.aws.boto3.client")
    def test_get_client_with_additional_kwargs(self, mock_boto3_client):
        AWSClientFactory.get_client("s3", use_ssl=False, verify=False)
        mock_boto3_client.assert_called_once_with(
            "s3",
            region_name=settings.s3_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url=settings.aws_s3_endpoint_url,
            use_ssl=False,
            verify=False,
        )


class TestGetS3Client:
    @patch("app.infrastructure.aws.AWSClientFactory.get_client")
    def test_get_s3_client_default(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        client = get_s3_client()
        mock_get_client.assert_called_once_with("s3", region_name=None)
        assert client == mock_client

    @patch("app.infrastructure.aws.AWSClientFactory.get_client")
    def test_get_s3_client_with_region(self, mock_get_client):
        get_s3_client(region_name="eu-west-1")
        mock_get_client.assert_called_once_with("s3", region_name="eu-west-1")
