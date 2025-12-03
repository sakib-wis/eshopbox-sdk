# EShopBox Python SDK

A comprehensive Python SDK for integrating with EShopBox Shipping APIs.

## Installation

```bash
pip install eshopbox-sdk
```

## Quick Start

```python
from eshopbox import EShopBoxSDK

sdk = EShopBoxSDK(
    workspace="your-workspace",
    client_id="your-client-id",
    client_secret="your-client-secret",
    refresh_token="your-refresh-token"
)

# Create an order
order = sdk.orders.create({...})
```

## Documentation

Full documentation coming soon.

## License

MIT License
