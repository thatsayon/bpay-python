from bpay.config.environments import (
    Environment,
)
from bpay.providers.bkash.agreement import (
    BkashAgreement,
)
from bpay.providers.bkash.auth import (
    BkashAuth,
)
from bpay.providers.bkash.constants import (
    BKASH_BASE_URLS,
)
from bpay.providers.bkash.payment import (
    BkashPayment,
)
from bpay.providers.bkash.schemas import (
    BkashCredentials,
)
from bpay.providers.bkash.verification import (
    BkashVerification,
)
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)
from bpay.schemas.verification import (
    PaymentVerificationResponse,
)


class BkashProvider:
    def __init__(
        self,
        username: str,
        password: str,
        app_key: str,
        app_secret: str,
        environment: Environment = (
            Environment.SANDBOX
        ),
    ) -> None:
        credentials = (
            BkashCredentials(
                username=username,
                password=password,
                app_key=app_key,
                app_secret=app_secret,
            )
        )

        base_url = (
            BKASH_BASE_URLS[
                environment.value
            ]
        )

        auth = BkashAuth(
            credentials=credentials,
            base_url=base_url,
        )

        self.agreement_service = (
            BkashAgreement(
                auth=auth,
                base_url=base_url,
            )
        )

        self.payment_service = (
            BkashPayment(
                auth=auth,
                base_url=base_url,
            )
        )

        self.verification_service = (
            BkashVerification(
                auth=auth,
                base_url=base_url,
            )
        )

    async def create_agreement(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
        return await (
            self.agreement_service.create(
                payload
            )
        )

    async def create_payment(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        return await (
            self.payment_service.create(
                payload
            )
        )

    async def verify_payment(
        self,
        payment_id: str,
    ) -> PaymentVerificationResponse:
        return await (
            self.verification_service.verify_payment(
                payment_id
            )
        )
