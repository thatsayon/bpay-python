from typing import Any

import httpx

from bpay.providers.bkash.schemas import (
    BkashCredentials,
    BkashTokenResponse,
)


class BkashAuth:
    BASE_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta"

    def __init__(self, credentials: BkashCredentials) -> None:
        self.credentials = credentials

    async def authenticate(self) -> BkashTokenResponse:
        url = f"{self.BASE_URL}/tokenized/checkout/token/grant"

        headers = {
            "Content-Type": "application/json",
            "username": self.credentials.username,
            "password": self.credentials.password,
        }

        payload = {
            "app_key": self.credentials.app_key,
            "app_secret": self.credentials.app_secret,
        }

        async with httpx.AsyncClient(timeout=30) as client:
            response = await client.post(
                url,
                json=payload,
                headers=headers,
            )

        response.raise_for_status()

        data: dict[str, Any] = response.json()

        return BkashTokenResponse(
            id_token=data["id_token"],
            refresh_token=data["refresh_token"],
            token_type=data["token_type"],
            expires_in=data["expires_in"],
        )
