from typing import Any

import httpx


class HttpTransport:
    def __init__(self) -> None:
        self.client = httpx.AsyncClient(timeout=30)

    async def post(
        self,
        url: str,
        **kwargs: Any,
    ) -> httpx.Response:
        return await self.client.post(url, **kwargs)
