import asyncio

from bpay.providers.bkash.auth import BkashAuth
from bpay.providers.bkash.schemas import BkashCredentials


async def main() -> None:
    credentials = BkashCredentials(
        username="sandboxTokenizedUser02",
        password="sandboxTokenizedUser02@12345",
        app_key="4f6o0cjiki2rfm34kfdadl1eqq",
        app_secret="2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b",
    )

    auth = BkashAuth(credentials=credentials)

    token = await auth.authenticate()

    print("Token Type:", token.token_type)
    print("Expires In:", token.expires_in)


if __name__ == "__main__":
    asyncio.run(main())
