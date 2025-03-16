from pydantic import BaseModel, validator


class PresignedURLRequest(BaseModel):
    filename: str
    type: str
    file_size: int

    @validator('filename')
    def validate_filename(cls, filename):
        if "." not in filename:
            raise ValueError('filename must include a file extension')
        return filename

    @validator('type')
    def validate_type(cls, type):
        valid_types = ["video", "image"]
        if type not in valid_types:
            raise ValueError(f'type must be one of {valid_types}')
        return type

    @validator('file_size')
    def validate_file_size(cls, file_size):
        max_size_gb = 5
        max_size_bytes = max_size_gb * 1024 * 1024 * 1024

        if file_size > max_size_bytes:
            raise ValueError(f'file_size must not exceed {max_size_gb} GB')

        if file_size <= 0:
            raise ValueError('file_size must be a positive integer')
        return file_size
