import pytest
from datetime import datetime
from uuid import UUID, uuid4
from pydantic import ValidationError

from app.schemas.response.update_file_status_response import UpdateFileStatusResponse


class TestUpdateFileStatusResponse:
    def test_valid_data(self):
        # Test with valid data
        test_uuid = uuid4()
        test_date = datetime.now()
        data = {
            "uuid": test_uuid,
            "name": "test_file.pdf",
            "type": "application/pdf",
            "status": "uploaded",
            "updated_at": test_date
        }

        response = UpdateFileStatusResponse(**data)
        
        assert response.uuid == test_uuid
        assert response.name == "test_file.pdf"
        assert response.type == "application/pdf"
        assert response.status == "uploaded"
        assert response.updated_at == test_date

    def test_from_orm(self):
        # Test from_orm method with a mock object
        test_uuid = uuid4()
        test_date = datetime.now()

        class MockFile:
            def __init__(self):
                self.uuid = test_uuid
                self.name = "test_file.docx"
                self.type = "application/docx"
                self.status = "processed"
                self.updated_at = test_date

        mock_file = MockFile()
        response = UpdateFileStatusResponse.from_orm(mock_file)
        
        assert response.uuid == test_uuid
        assert response.name == "test_file.docx"
        assert response.type == "application/docx"
        assert response.status == "processed"
        assert response.updated_at == test_date

    def test_missing_fields(self):
        # Test with missing required fields
        with pytest.raises(ValidationError):
            UpdateFileStatusResponse(
                name="test_file.pdf",
                type="application/pdf",
                status="uploaded",
                updated_at=datetime.now()
                # Missing uuid
            )
