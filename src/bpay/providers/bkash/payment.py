from typing import Any

import httpx

from bpay.exceptions import (
    ProviderAPIError,
)
from bpay.providers.bkash.auth import (
    BkashAuth,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)
from bpay.types import PaymentStatus


class BkashPayment:
    def __init__(
        self,
        auth: BkashAuth,
        base_url: str,
    ) -> None:
        self.auth = auth
        self.base_url = base_url

    async def create(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        token = await self.auth.get_token()

        url = (
            f"{self.base_url}"
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
            "payerReference": (
                payload.payer_reference or ""
            ),
            "callbackURL": (
                payload.callback_url
            ),
            "amount": str(
                payload.amount
            ),
            "currency": (
                payload.currency
            ),
            "intent": (
                payload.intent
            ),
            "merchantInvoiceNumber": (
                payload.merchant_invoice_number
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
                f"Payment creation failed: "
                f"{data}"
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
