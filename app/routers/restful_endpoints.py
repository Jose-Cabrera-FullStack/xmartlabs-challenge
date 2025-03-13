from fastapi import APIRouter, HTTPException
from ormar import NoMatch

# from app.schemas.request import (
#     DebtCreatePOSTRequest,
#     DebtUpdatePATCHRequest,
#     DebtListIdsPOSTRequest,
# )
# from app.schemas.response import (
#     DebtStatusGETResponse,
#     DebtStatusPATCHResponse,
# )
# from app.schemas.response.http_response import SuccessResponse
# from app.service import DebtService
# from app.exceptions.custom_exception import (
#     BadRequestException,
#     InternalServerErrorException,
#     UniqueIdentifierGenerationError,
# )

# Example of a RESTful endpoint
router = APIRouter(prefix="/v1/debts", tags=["debts"])

# @router.post("/")
# async def create_debt_endpoint(post_request: DebtCreatePOSTRequest):
#     try:
#         service_payment = await DebtService.create_debt(post_request.dict())
#         return SuccessResponse(data=service_payment)
#     except BadRequestException as e:
#         raise HTTPException(status_code=400, detail=f"The debt to be updated was not found. Error: {e}")
#     except UniqueIdentifierGenerationError as e:
#         raise HTTPException(status_code=503, detail=f"Unique Identifier Generation Error. Please try again.")
#     except InternalServerErrorException as e:
#         raise HTTPException(status_code=500, detail=f"Error updating the debt. The error is: {e}")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error updating the debt. The error is: {e}")

# @router.post("/status")
# async def get_debts_status(post_request: DebtListIdsPOSTRequest):
#     try:
#         service_payment = await DebtService.get_debts_status_by_id(post_request.dict()["operation_identifiers"])
#         return SuccessResponse(data=service_payment)
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error getting the debts status. The error is: {e}")

# @router.get("/{operation_identifier}", response_model=DebtStatusGETResponse, status_code=200)
# async def get_debt_status(operation_identifier: str):
#     try:
#         debt_status_response = await DebtService.get_debt_status(operation_identifier)
#         return DebtStatusGETResponse(**debt_status_response)
#     except BadRequestException as e:
#         raise HTTPException(status_code=400, detail=str(e))
#     except NoMatch as e:
#         raise HTTPException(status_code=404, detail=str(e))
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error getting the debt status. The error is: {e}")

# @router.patch("/")
# async def update_debt_payment(patch_request: DebtUpdatePATCHRequest):
#     try:
#         update_service = await DebtService.update_debt_payment(patch_request.dict())
#         return DebtStatusPATCHResponse(**update_service)
#     except NoMatch as e:
#         raise HTTPException(status_code=404, detail="The debt to be updated was not found.")
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error updating the debt. The error is: {e}")
