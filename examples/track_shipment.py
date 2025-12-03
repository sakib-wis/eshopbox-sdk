"""
Example: Track shipment using EShopBox SDK
"""

from eshopbox import EShopBoxSDK


def main():
    sdk = EShopBoxSDK(
        workspace="your_workspace",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        refresh_token="REFRESH_TOKEN"
    )

    tracking_number = "AWB123456789"

    print(f"Tracking shipment: {tracking_number}")
    result = sdk.shipments.track(tracking_number)

    print("Tracking Details:")
    print(result)


if __name__ == "__main__":
    main()
