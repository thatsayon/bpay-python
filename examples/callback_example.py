from bpay.providers.bkash.callbacks import (
    parse_agreement_callback,
)

params = {
    "paymentID": "TR001",
    "status": "success",
    "signature": "abc123",
    "agreementID": "AGR001",
}

callback = parse_agreement_callback(params)

print(callback)
