from bpay.providers.bkash.agreement import (
    BkashAgreement,
)
from bpay.providers.bkash.auth import BkashAuth
from bpay.providers.bkash.schemas import (
    BkashCredentials,
)
from bpay.schemas.agreement import (
    AgreementResponse,
    CreateAgreementRequest,
)


class BkashProvider:
    def __init__(
        self,
        username: str,
        password: str,
        app_key: str,
        app_secret: str,
    ) -> None:
        credentials = BkashCredentials(
            username=username,
            password=password,
            app_key=app_key,
            app_secret=app_secret,
        )

        auth = BkashAuth(credentials)

        self.agreement_service = BkashAgreement(auth)

    async def create_agreement(
        self,
        payload: CreateAgreementRequest,
    ) -> AgreementResponse:
        return await self.agreement_service.create(payload)
