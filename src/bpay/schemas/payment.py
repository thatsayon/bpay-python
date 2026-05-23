from pydantic import BaseModel, HttpUrl

from bpay.types import PaymentStatus


class CreatePaymentRequest(BaseModel):
    amount: float
    callback_url: HttpUrl
    currency: str = "BDT"
    intent: str = "sale"


class PaymentResponse(BaseModel):
    payment_id: str
    checkout_url: HttpUrl
    status: PaymentStatus
