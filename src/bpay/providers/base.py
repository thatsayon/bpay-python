from abc import ABC, abstractmethod

from bpay.schemas.payment import (
    CreatePaymentRequest,
    PaymentResponse,
)


class BaseProvider(ABC):
    @abstractmethod
    async def create_payment(
        self,
        payload: CreatePaymentRequest,
    ) -> PaymentResponse:
        pass
