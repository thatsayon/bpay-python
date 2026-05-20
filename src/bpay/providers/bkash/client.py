from bpay.providers.base import BaseProvider
from bpay.schemas.payment import PaymentResponse


class BkashProvider(BaseProvider):
    async def create_payment(self) -> PaymentResponse:
        return PaymentResponse(
            provider="bkash",
            action="create_payment",
        )

    async def verify_payment(self) -> PaymentResponse:
        return PaymentResponse(
            provider="bkash",
            action="verify_payment",
        )

    async def refund_payment(self) -> PaymentResponse:
        return PaymentResponse(
            provider="bkash",
            action="refund_payment",
        )
