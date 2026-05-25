from bpay.schemas.payment_callback import (
    PaymentCallback,
)
from bpay.types import PaymentStatus

STATUS_MAP = {
    "success": PaymentStatus.SUCCESS,
    "failure": PaymentStatus.FAILED,
    "cancel": PaymentStatus.CANCELLED,
}


def parse_payment_callback(
    params: dict[str, str],
) -> PaymentCallback:
    return PaymentCallback(
        payment_id=params["paymentID"],
        status=STATUS_MAP[
            params["status"]
        ],
        signature=params["signature"],
    )
