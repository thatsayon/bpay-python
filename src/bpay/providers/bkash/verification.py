from typing import Any

import httpx

from bpay.exceptions import (
    ProviderAPIError,
)
from bpay.providers.bkash.auth import (
    BkashAuth,
)
from bpay.schemas.verification import (
    PaymentVerificationResponse,
)
from bpay.types import PaymentStatus


class BkashVerification:
    def __init__(
        self,
        auth: BkashAuth,
        base_url: str,
    ) -> None:
        self.auth = auth
        self.base_url = base_url

    async def verify_payment(
        self,
        payment_id: str,
    ) -> PaymentVerificationResponse:
        token = await self.auth.get_token()

        url = (
            f"{self.base_url}"
            "/tokenized/checkout/payment/status"
        )

        headers = {
            "Authorization": (
                f"Bearer {token}"
            ),
            "X-APP-Key": (
                self.auth.credentials.app_key
            ),
        }

        payload = {
            "paymentID": payment_id
        }

        async with httpx.AsyncClient(
            timeout=30
        ) as client:
            response = await client.post(
                url,
                json=payload,
                headers=headers,
            )

        response.raise_for_status()

        data: dict[str, Any] = (
            response.json()
        )

        if data.get("statusCode") != "0000":
            raise ProviderAPIError(
                f"Payment verification failed: "
                f"{data}"
            )

        return (
            PaymentVerificationResponse(
                payment_id=str(
                    data["paymentID"]
                ),
                trx_id=data.get("trxID"),
                amount=float(
                    data.get("amount", 0)
                ),
                status=(
                    PaymentStatus.SUCCESS
                ),
            )
        )
