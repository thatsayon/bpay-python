from typing import Any

import httpx

from bpay.providers.bkash.auth import BkashAuth
from bpay.providers.bkash.constants import (
    BKASH_AGREEMENT_STATUS_MAP,
)
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)


class BkashAgreement:
    BASE_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta"

    def __init__(self, auth: BkashAuth) -> None:
        self.auth = auth

    async def create(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
        token = await self.auth.authenticate()

        url = (
            f"{self.BASE_URL}"
            "/tokenized/checkout/create"
        )

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token.id_token}",
            "X-APP-Key": self.auth.credentials.app_key,
        }

        request_body = {
            "mode": "0000",
            "payerReference": payload.customer_phone,
            "callbackURL": payload.callback_url,
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                url,
                json=request_body,
                headers=headers,
            )

        response.raise_for_status()

        data: dict[str, Any] = response.json()
        
        return AgreementResponse(
            agreement_id="",
            payment_id=str(data["paymentID"]),
            checkout_url=str(data["bkashURL"]),
            status=BKASH_AGREEMENT_STATUS_MAP[
                str(data["agreementStatus"])
            ],
        )
