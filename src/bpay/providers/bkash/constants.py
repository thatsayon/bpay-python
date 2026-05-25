from bpay.types import AgreementStatus


BKASH_AGREEMENT_STATUS_MAP = {
    "Initiated": AgreementStatus.INITIATED,
    "Completed": AgreementStatus.ACTIVE,
    "Cancelled": AgreementStatus.CANCELLED,
    "Failure": AgreementStatus.FAILED,
}
