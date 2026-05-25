# bpay

Unified Python SDK for Bangladeshi payment gateways.

`bpay` provides a clean, typed, async-first developer experience for integrating Bangladeshi payment providers like bKash, Nagad, and SSLCommerz.

---

## Features

- Async-first architecture
- Typed request & response models
- Sandbox & production environment support
- Hosted checkout workflows
- Agreement/tokenized checkout support
- Payment callback parsing
- Payment verification support
- Provider abstraction layer
- Modern Python packaging with `uv`

---

## Supported Providers

| Provider | Status |
|---|---|
| bKash | In Progress |
| Nagad | Planned |
| SSLCommerz | Planned |

---

## Installation

```bash
pip install bpay
```

---

## Quick Start

### Create a One-Time Payment

```python
import asyncio

from bpay import BPay
from bpay.config.environments import (
    Environment,
)
from bpay.schemas.payment import (
    CreatePaymentRequest,
)


async def main() -> None:
    client = BPay(
        provider="bkash",
        environment=Environment.SANDBOX,
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        app_key="YOUR_APP_KEY",
        app_secret="YOUR_APP_SECRET",
    )

    payment = await client.create_payment(
        CreatePaymentRequest(
            amount=100,
            merchant_invoice_number="INV-1001",
            callback_url=(
                "https://yourdomain.com/callback"
            ),
        )
    )

    print(payment.checkout_url)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Agreement / Tokenized Checkout

Agreements allow merchants to create reusable customer payment authorizations for recurring or saved payments.

### Create Agreement

```python
import asyncio

from bpay import BPay
from bpay.config.environments import (
    Environment,
)
from bpay.schemas.agreement import (
    CreateAgreementRequest,
)


async def main() -> None:
    client = BPay(
        provider="bkash",
        environment=Environment.SANDBOX,
        username="YOUR_USERNAME",
        password="YOUR_PASSWORD",
        app_key="YOUR_APP_KEY",
        app_secret="YOUR_APP_SECRET",
    )

    agreement = await (
        client.create_agreement(
            CreateAgreementRequest(
                customer_phone="017XXXXXXXX",
                callback_url=(
                    "https://yourdomain.com/callback"
                ),
            )
        )
    )

    print(agreement.checkout_url)


if __name__ == "__main__":
    asyncio.run(main())
```

---

## Callback Parsing

### Payment Callback

```python
from bpay import BPay

client = BPay(...)

callback = client.parse_payment_callback(
    {
        "paymentID": "PAY123",
        "status": "success",
        "signature": "abc123",
    }
)

print(callback.status)
```

---

### Agreement Callback

```python
from bpay import BPay

client = BPay(...)

callback = (
    client.parse_agreement_callback(
        {
            "paymentID": "PAY123",
            "agreementID": "AGR123",
            "status": "success",
            "signature": "abc123",
        }
    )
)

print(callback.status)
```

---

## Payment Verification

```python
verification = await client.verify_payment(
    payment_id="PAY123"
)

print(verification.status)
```

---

## Environments

`bpay` supports both sandbox and production environments.

### Sandbox

```python
from bpay.config.environments import (
    Environment,
)

Environment.SANDBOX
```

### Production

```python
from bpay.config.environments import (
    Environment,
)

Environment.PRODUCTION
```

---

## Development

### Setup

```bash
uv sync
```

### Run Checks

```bash
make check
```

### Run Tests

```bash
uv run pytest
```

---

## Project Structure

```text
src/bpay/
├── client.py
├── exceptions.py
├── config/
├── providers/
├── schemas/
├── transports/
└── types.py
```

---

## Roadmap

- Full bKash recurring payment workflow
- Nagad integration
- SSLCommerz integration
- Refund support
- Webhook signature verification
- Automatic retry handling
- Sync client support
- Logging middleware

---

## License

MIT License
