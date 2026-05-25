from pydantic import BaseModel

from bpay.types import PaymentStatus


class PaymentVerificationResponse(
    BaseModel
):
    payment_id: str
    trx_id: str | None = None
    amount: float | None = None
    status: PaymentStatus
