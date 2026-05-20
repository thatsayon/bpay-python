from bpay.client import BPay


def test_bkash_provider_selection() -> None:
    client = BPay(provider="bkash")

    assert client.provider is not None
