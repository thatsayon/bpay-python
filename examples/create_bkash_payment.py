import asyncio

from bpay import BPay
from bpay.config.environments import (
    Environment,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
)


async def main() -> None:
    client = BPay(
        provider="bkash",
        environment=Environment.SANDBOX,
        username="sandboxTokenizedUser02",
        password="sandboxTokenizedUser02@12345",
        app_key="4f6o0cjiki2rfm34kfdadl1eqq",
        app_secret="2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b",
    )

    payment = await (
        client.create_payment(
            CreatePaymentRequest(
                amount=100,
                callback_url=(
                    "https://merchantdemo."
                    "sandbox.bka.sh/callback"
                ),
            )
        )
    )

    print(payment)


if __name__ == "__main__":
    asyncio.run(main())
