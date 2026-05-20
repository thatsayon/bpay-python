from abc import ABC, abstractmethod

from bpay.schemas.payment import PaymentResponse


class BaseProvider(ABC):
    @abstractmethod
    async def create_payment(self) -> PaymentResponse:
        pass

    @abstractmethod
    async def verify_payment(self) -> PaymentResponse:
        pass

    @abstractmethod
    async def refund_payment(self) -> PaymentResponse:
        pass
