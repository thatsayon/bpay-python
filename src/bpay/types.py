from enum import StrEnum


class PaymentStatus(StrEnum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"
    CANCELLED = "cancelled"


class RefundStatus(StrEnum):
    PENDING = "pending"
    SUCCESS = "success"
    FAILED = "failed"


class AgreementStatus(StrEnum):
    INITIATED = "initiated"
    ACTIVE = "active"
    FAILED = "failed"
    CANCELLED = "cancelled"
