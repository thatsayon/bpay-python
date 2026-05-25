class BPayError(Exception):
    """Base exception for all bpay errors."""


class AuthenticationError(BPayError):
    """Raised when provider authentication fails."""


class AgreementError(BPayError):
    """Raised when agreement workflow fails."""


class ProviderAPIError(BPayError):
    """Raised when provider API returns unexpected response."""
