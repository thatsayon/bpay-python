from bpay.providers.bkash.callbacks import (
    parse_agreement_callback,
)
from bpay.types import (
    AgreementStatus,
)


def test_parse_agreement_callback(
) -> None:
    params = {
        "paymentID": "PAY123",
        "status": "success",
        "signature": "abc",
        "agreementID": "AGR123",
    }

    callback = (
        parse_agreement_callback(
            params
        )
    )

    assert (
        callback.agreement_id
        == "AGR123"
    )

    assert (
        callback.status
        == AgreementStatus.ACTIVE
    )
