from typing import Any

from bpay.providers.bkash.callbacks import (
    parse_agreement_callback,
)
from bpay.providers.bkash.payment_callbacks import (
    parse_payment_callback,
)
from bpay.providers.registry import (
    PROVIDERS,
)
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)
from bpay.schemas.callback import (
    AgreementCallback,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)
from bpay.schemas.payment_callback import (
    PaymentCallback,
)
from bpay.schemas.verification import (
    PaymentVerificationResponse,
)


class BPay:
    def __init__(
        self,
        provider: str,
        **credentials: Any,
    ) -> None:
        provider_class = (
            PROVIDERS.get(provider)
        )

        if provider_class is None:
            supported = ", ".join(
                PROVIDERS.keys()
            )

            raise ValueError(
                f"Unsupported provider: "
                f"{provider}. "
                f"Supported providers: "
                f"{supported}"
            )

        self.provider_name = (
            provider
        )

        self.provider = (
            provider_class(
                **credentials
            )
        )

    async def create_agreement(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
        if not hasattr(
            self.provider,
            "create_agreement",
        ):
            raise NotImplementedError(
                f"{self.provider_name} "
                "does not support "
                "agreement creation"
            )

        return await (
            self.provider.create_agreement(
                payload
            )
        )

    async def create_payment(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        if not hasattr(
            self.provider,
            "create_payment",
        ):
            raise NotImplementedError(
                f"{self.provider_name} "
                "does not support "
                "payment creation"
            )

        return await (
            self.provider.create_payment(
                payload
            )
        )

    def parse_agreement_callback(
        self,
        params: dict[str, str],
    ) -> AgreementCallback:
        if (
            self.provider_name
            != "bkash"
        ):
            raise NotImplementedError(
                f"{self.provider_name} "
                "does not support "
                "agreement callbacks yet"
            )

        return (
            parse_agreement_callback(
                params
            )
        )

    def parse_payment_callback(
        self,
        params: dict[str, str],
    ) -> PaymentCallback:
        if self.provider_name != "bkash":
            raise NotImplementedError(
                f"{self.provider_name} "
                "does not support "
                "payment callbacks yet"
            )

        return parse_payment_callback(
            params
        )

    async def verify_payment(
        self,
        payment_id: str,
    ) -> PaymentVerificationResponse:
        if not hasattr(
            self.provider,
            "verify_payment",
        ):
            raise NotImplementedError(
                f"{self.provider_name} "
                "does not support "
                "payment verification"
            )

        return await (
            self.provider.verify_payment(
                payment_id
            )
        )

