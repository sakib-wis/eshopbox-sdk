"""
Example: Create a new order using EShopBox SDK
"""

from eshopbox import EShopBoxSDK


def main():
    # Initialize SDK
    sdk = EShopBoxSDK(
        workspace="your_workspace",
        client_id="CLIENT_ID",
        client_secret="CLIENT_SECRET",
        refresh_token="REFRESH_TOKEN"
    )

    # Example order payload
    order_data = {
        "externalChannelID": "ECOM001",
        "customerOrderNumber": "ORD10001",
        "customerDetails": {
            "name": "John Doe",
            "email": "john@example.com",
            "phone": "9876543210"
        },
        "shippingAddress": {
            "address1": "221B Baker Street",
            "city": "London",
            "state": "London",
            "pincode": "560001",
            "country": "UK"
        },
        "items": [
            {
                "sku": "SKU1234",
                "quantity": 1,
                "sellingPrice": 499.0
            }
        ]
    }

    print("Creating order...")
    response = sdk.orders.create(order_data)

    print("Order created successfully!")
    print(response)


if __name__ == "__main__":
    main()
