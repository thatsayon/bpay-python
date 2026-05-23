from pydantic import HttpUrl

from bpay.providers.base import BaseProvider
from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)
from bpay.types import PaymentStatus


class BkashProvider(BaseProvider):
    async def create_payment(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        return PaymentResponse(
            payment_id="demo_payment",
            checkout_url=HttpUrl("https://sandbox.payment.bkash.com"),
            status=PaymentStatus.PENDING,
        )
