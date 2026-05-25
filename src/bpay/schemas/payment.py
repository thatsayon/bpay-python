from pydantic import BaseModel

from bpay.types import PaymentStatus


class CreatePaymentRequest(BaseModel):
    amount: float
    callback_url: str
    merchant_invoice_number: str

    currency: str = "BDT"
    intent: str = "sale"

    payer_reference: str | None = None


class PaymentResponse(BaseModel):
    payment_id: str
    checkout_url: str
    status: PaymentStatus
