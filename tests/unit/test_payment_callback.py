from bpay.providers.bkash.payment_callbacks import (
    parse_payment_callback,
)
from bpay.types import PaymentStatus


def test_parse_payment_callback() -> None:
    params = {
        "paymentID": "PAY123",
        "status": "success",
        "signature": "abc",
    }

    callback = parse_payment_callback(
        params
    )

    assert (
        callback.payment_id
        == "PAY123"
    )

    assert (
        callback.status
        == PaymentStatus.SUCCESS
    )
