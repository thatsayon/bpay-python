from typing import Any

import httpx

from bpay.exceptions import ProviderAPIError
from bpay.providers.bkash.auth import (
    BkashAuth,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)
from bpay.types import PaymentStatus


class BkashPayment:
    BASE_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta"

    def __init__(
        self,
        auth: BkashAuth,
    ) -> None:
        self.auth = auth

    async def create(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        token = await self.auth.get_token()

        url = (
            f"{self.BASE_URL}"
            "/tokenized/checkout/create"
        )

        headers = {
            "Content-Type": "application/json",
            "Authorization": (
                f"Bearer {token}"
            ),
            "X-APP-Key": (
                self.auth.credentials.app_key
            ),
        }

        request_body = {
            "mode": "0011",
            "payerReference": "01770618575",
            "callbackURL": str(
                payload.callback_url
            ),
            "amount": str(payload.amount),
            "currency": payload.currency,
            "intent": payload.intent,
            "merchantInvoiceNumber": (
                "INV-0001"
            ),
        }

        async with httpx.AsyncClient(
            timeout=30
        ) as client:
            response = await client.post(
                url,
                json=request_body,
                headers=headers,
            )

        response.raise_for_status()

        data: dict[str, Any] = (
            response.json()
        )

        if data.get("statusCode") != "0000":
            raise ProviderAPIError(
                f"Payment creation failed: {data}"
            )

        return PaymentResponse(
            payment_id=str(
                data["paymentID"]
            ),
            checkout_url=str(
                data["bkashURL"]
            ),
            status=PaymentStatus.PENDING,
        )
