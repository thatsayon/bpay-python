import asyncio

from bpay.client import BPay


async def main() -> None:
    client = BPay(provider="bkash")

    result = await client.provider.create_payment()

    print(result)


asyncio.run(main())
