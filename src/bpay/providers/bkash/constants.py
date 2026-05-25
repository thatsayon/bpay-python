from bpay.types import AgreementStatus

BKASH_AGREEMENT_STATUS_MAP = {
    "Initiated": AgreementStatus.INITIATED,
    "Completed": AgreementStatus.ACTIVE,
    "Cancelled": AgreementStatus.CANCELLED,
    "Failure": AgreementStatus.FAILED,
}

BKASH_BASE_URLS = {
    "sandbox": (
        "https://tokenized.sandbox.bka.sh/v1.2.0-beta"
    ),
    "production": (
        "https://tokenized.pay.bka.sh/v1.2.0-beta"
    ),
}
