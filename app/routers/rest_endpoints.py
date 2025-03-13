from fastapi import APIRouter

# from app.schemas.request import (
#     PaymentUpdatePOSTRequest,
#     RevertDebtPaymentPOSTRequest,
#     DebtStatusPOSTRequest
# )
# from app.schemas.response import (
#     DebtUpdatePOSTResponse,
#     DebtStatusPOSTResponse,
#     RevertDebtPaymentPOSTResponse,
# )
# from app.service import PaymentService, DebtService

# Example of a REST endpoint
router = APIRouter(prefix="/v1", tags=["payments"])

# @router.post("/debt-status", response_model=DebtStatusPOSTResponse, status_code=200)
# async def payment_post_endpoint(post_request: DebtStatusPOSTRequest):
#     service_payment = await DebtService.debt_status(post_request.dict())
#     return DebtStatusPOSTResponse(**service_payment)

# @router.post("/update-debt-payment", response_model=DebtUpdatePOSTResponse, status_code=200)
# async def update_debt_payment_endpoint(post_request: PaymentUpdatePOSTRequest):
#     debt_service = await PaymentService.update_debt_payment(post_request.dict())
#     return DebtUpdatePOSTResponse(**debt_service)

# @router.post("/revert-debt-payment", response_model=RevertDebtPaymentPOSTResponse, status_code=200)
# async def revert_debt_payment_endpoint(post_request: RevertDebtPaymentPOSTRequest):
#     reverse_service = await PaymentService.revert_payment_debt(post_request.dict())
#     return RevertDebtPaymentPOSTResponse(**reverse_service)
