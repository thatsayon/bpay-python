from bpay.schemas.callback import (
    AgreementCallback,
)
from bpay.types import AgreementStatus

STATUS_MAP = {
    "success": AgreementStatus.ACTIVE,
    "failure": AgreementStatus.FAILED,
    "cancel": AgreementStatus.CANCELLED,
}


def parse_agreement_callback(
    params: dict[str, str],
) -> AgreementCallback:
    return AgreementCallback(
        payment_id=params["paymentID"],
        status=STATUS_MAP[params["status"]],
        signature=params["signature"],
        agreement_id=params.get("agreementID"),
    )
