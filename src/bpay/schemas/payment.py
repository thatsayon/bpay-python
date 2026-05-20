from pydantic import BaseModel


class PaymentResponse(BaseModel):
    provider: str
    action: str
