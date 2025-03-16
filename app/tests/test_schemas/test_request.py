import pytest

from app.schemas.request.presigned_url_request import PresignedURLRequest


def test_presigned_url_request_valid():
    data = {
        "filename": "test.txt",
        "type": "image",
        "file_size": 1024
    }
    request = PresignedURLRequest(**data)
    assert request.filename == "test.txt"
    assert request.type == "image"
    assert request.file_size == 1024


def test_presigned_url_request_invalid_filename():
    with pytest.raises(ValueError):
        PresignedURLRequest(filename="testfile", type="image", file_size=1024)


def test_presigned_url_request_invalid_type():
    with pytest.raises(ValueError):
        PresignedURLRequest(filename="test.txt", type="document", file_size=1024)


def test_presigned_url_request_invalid_file_size():
    with pytest.raises(ValueError):
        PresignedURLRequest(filename="test.txt", type="video", file_size=-1024)


def test_presigned_url_request_file_size_too_large():
    max_size_gb = 5
    too_large_size = (max_size_gb * 1024 * 1024 * 1024) + 1
    with pytest.raises(ValueError, match=f'file_size must not exceed {max_size_gb} GB'):
        PresignedURLRequest(filename="test.txt", type="image", file_size=too_large_size)
