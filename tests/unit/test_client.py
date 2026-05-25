from bpay.client import BPay


def test_bkash_provider_selection() -> None:
    client = BPay(
        provider="bkash",
        username="sandboxTokenizedUser02",
        password="sandboxTokenizedUser02@12345",
        app_key="4f6o0cjiki2rfm34kfdadl1eqq",
        app_secret="2is7hdktrekvrbljjh44ll3d9l1dtjo4pasmjvs5vl5qr3fug4b",
    )

    assert client.provider is not None
