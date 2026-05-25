from typing import Any

import httpx

from bpay.exceptions import AgreementError
from bpay.providers.bkash.auth import (
    BkashAuth,
)
from bpay.providers.bkash.constants import (
    BKASH_AGREEMENT_STATUS_MAP,
)
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)


class BkashAgreement:
    def __init__(
        self,
        auth: BkashAuth,
        base_url: str,
    ) -> None:
        self.auth = auth
        self.base_url = base_url

    async def create(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
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
            "mode": "0000",
            "payerReference": (
                payload.customer_phone
            ),
            "callbackURL": (
                payload.callback_url
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
            raise AgreementError(
                f"Agreement creation failed: "
                f"{data}"
            )

        return AgreementResponse(
            agreement_id="",
            payment_id=str(
                data["paymentID"]
            ),
            checkout_url=str(
                data["bkashURL"]
            ),
            status=(
                BKASH_AGREEMENT_STATUS_MAP[
                    str(
                        data[
                            "agreementStatus"
                        ]
                    )
                ]
            ),
        )
