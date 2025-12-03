"""
Example: Setup webhook using EShopBox SDK
"""

from eshopbox import EShopBoxSDK


def main():
    sdk = EShopBoxSDK(
        workspace="your_workspace",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        refresh_token="REFRESH_TOKEN"
    )

    print("Registering webhook...")

    payload = {
        "event": "order.created",
        "callbackUrl": "https://yourapp.com/webhooks/eshopbox",
        "active": True
    }

    response = sdk.webhooks.create(payload)

    print("Webhook registered successfully!")
    print(response)


if __name__ == "__main__":
    main()
