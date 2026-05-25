class BPayError(Exception):
    """Base exception for bpay."""


class AuthenticationError(
    BPayError
):
    """Authentication failed."""


class AgreementError(
    BPayError
):
    """Agreement workflow failed."""


class ProviderAPIError(
    BPayError
):
    def __init__(
        self,
        message: str,
        provider_code: (
            str | None
        ) = None,
    ) -> None:
        self.provider_code = (
            provider_code
        )

        super().__init__(message)
