from pydantic import BaseModel

from bpay.types import AgreementStatus


class CreateAgreementRequest(BaseModel):
    customer_phone: str
    callback_url: str


class AgreementResponse(BaseModel):
    agreement_id: str
    payment_id: str
    checkout_url: str
    status: AgreementStatus
