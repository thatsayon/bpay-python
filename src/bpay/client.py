from typing import Any

from bpay.providers.bkash.callbacks import (
    parse_agreement_callback,
)
from bpay.providers.registry import PROVIDERS
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)
from bpay.schemas.callback import (
    AgreementCallback,
)


class BPay:
    def __init__(
        self,
        provider: str,
        **credentials: Any,
    ) -> None:
        provider_class = PROVIDERS.get(provider)

        if provider_class is None:
            supported = ", ".join(PROVIDERS.keys())

            raise ValueError(
                f"Unsupported provider: {provider}. Supported providers: {supported}"
            )

        self.provider_name = provider
        self.provider = provider_class(**credentials)

    async def create_agreement(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
        if not hasattr(
            self.provider,
            "create_agreement",
        ):
            raise NotImplementedError(
                f"{self.provider_name} does not support agreement creation"
            )

        return await self.provider.create_agreement(payload)

    def parse_agreement_callback(
        self,
        params: dict[str, str],
    ) -> AgreementCallback:
        if self.provider_name != "bkash":
            raise NotImplementedError(
                f"{self.provider_name} does not support agreement callbacks yet"
            )

        return parse_agreement_callback(params)
