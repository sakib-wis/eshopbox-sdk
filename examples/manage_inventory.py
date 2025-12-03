"""
Example: Manage Inventory using EShopBox SDK
"""

from eshopbox import EShopBoxSDK


def main():
    sdk = EShopBoxSDK(
        workspace="your_workspace",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        refresh_token="REFRESH_TOKEN"
    )

    sku = "SKU1234"

    print(f"Fetching inventory for {sku}...")
    inventory = sdk.inventory.get_stock(sku)
    print("Current stock:", inventory)

    print(f"Updating inventory for {sku}...")
    update_payload = {
        "sku": sku,
        "quantity": 25
    }

    updated = sdk.inventory.update_stock(update_payload)
    print("Updated stock:", updated)


if __name__ == "__main__":
    main()
