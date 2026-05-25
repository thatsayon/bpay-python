import asyncio

from bpay import BPay
from bpay.schemas.agreement import (
    CreateAgreementRequest,
)


async def main() -> None:
    client = BPay(
        provider="bkash",
        username="sandboxTokenizedUser02",
        password="sandboxTokenizedUser02@12345",
        app_key="4f6o0cjiki2rfm34kfdadl1eqq",
        app_secret="2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b",
    )

    agreement = await client.create_agreement(
        CreateAgreementRequest(
            customer_phone="01733280204",
            callback_url=("https://youtube.com"),
        )
    )

    print(agreement)


if __name__ == "__main__":
    asyncio.run(main())
