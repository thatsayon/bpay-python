from pydantic import BaseModel

from bpay.types import AgreementStatus


class AgreementCallback(BaseModel):
    payment_id: str
    status: AgreementStatus
    signature: str
    agreement_id: str | None = None
