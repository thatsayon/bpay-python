from pydantic import BaseModel

from bpay.types import PaymentStatus


class PaymentCallback(BaseModel):
    payment_id: str
    status: PaymentStatus
    signature: str
