from bpay.providers.bkash.client import BkashProvider


class BPay:
    def __init__(self, provider: str) -> None:
        if provider == "bkash":
            self.provider = BkashProvider()
        else:
            raise ValueError("Unsupported provider")
