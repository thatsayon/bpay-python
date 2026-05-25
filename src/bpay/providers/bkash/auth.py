from datetime import UTC, datetime, timedelta
from typing import Any

import httpx

from bpay.exceptions import AuthenticationError
from bpay.providers.bkash.schemas import (
    BkashCredentials,
    BkashTokenResponse,
)


class BkashAuth:
    BASE_URL = "https://tokenized.sandbox.bka.sh/v1.2.0-beta"

    def __init__(
        self,
        credentials: BkashCredentials,
        base_url: str
    ) -> None:
        self.credentials = credentials
        self.base_url = base_url

        self._token: BkashTokenResponse | None = None
        self._expires_at: datetime | None = None

    async def authenticate(
        self,
    ) -> BkashTokenResponse:
        url = f"{self.base_url}/tokenized/checkout/token/grant"

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

        if data.get("statusCode") != "0000":
            raise AuthenticationError(f"bKash authentication failed: {data}")

        return BkashTokenResponse(
            id_token=str(data["id_token"]),
            refresh_token=str(data["refresh_token"]),
            token_type=str(data["token_type"]),
            expires_in=int(data["expires_in"]),
        )

    async def get_token(self) -> str:
        if (
            self._token is not None
            and self._expires_at is not None
            and datetime.now(UTC) < self._expires_at
        ):
            return self._token.id_token

        token = await self.authenticate()

        self._token = token

        self._expires_at = datetime.now(UTC) + timedelta(seconds=token.expires_in - 60)

        return token.id_token
