import asyncio

from bpay.providers.bkash.agreement import (
    BkashAgreement,
)
from bpay.providers.bkash.auth import BkashAuth
from bpay.providers.bkash.schemas import (
    BkashCredentials,
)
from bpay.schemas.agreement import (
    CreateAgreementRequest,
)


async def main() -> None:
    credentials = BkashCredentials(
        username="sandboxTokenizedUser02",
        password="sandboxTokenizedUser02@12345",
        app_key="4f6o0cjiki2rfm34kfdadl1eqq",
        app_secret="2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b",
    )

    auth = BkashAuth(credentials)

    agreement_service = BkashAgreement(auth)

    agreement = await agreement_service.create(
        CreateAgreementRequest(
            customer_phone="01733280204",
            callback_url=(
                "https://merchantdemo.sandbox.bka.sh/"
                "callback"
            ),
        )
    )

    print(agreement)


if __name__ == "__main__":
    asyncio.run(main())
