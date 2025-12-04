"""
Example: Setup Wrapper using EShopBox SDK
"""

from eshopbox import EShopBoxSDK
import os
from dotenv import load_dotenv
load_dotenv()


def get_all_payments(sdk):
    response = sdk.payments.get_all()
    print(response)


def get(sdk):
    params = {
        "neftId": "neftId"
    }
    response = sdk.payments.get(params)
    print(response)


def create(sdk):
    payload = {
        "fundTransferDate": "2018-09-25 05:30:00",
        "fundTransferAmount": 819901.7199999853,
        "transactionId": "lime3",
        "comments": "Limeroad Testing",
        "ledgerGroupId": "limeroad",
        "portalAccountId": 122,
        "reportUrl": "https://cdn.filestackcontent.com/ckdksjkasl676678687as"
    }
    response = sdk.payments.create(payload)
    print(response)


def main():
    # Initialize SDK
    sdk = EShopBoxSDK(
        workspace=os.getenv('ESHOPBOX_WORKSPACE', ''),
        client_id=os.getenv('ESHOPBOX_CLIENT_ID', ''),
        client_secret=os.getenv('ESHOPBOX_SECRET_ID', ''),
        refresh_token=os.getenv('ESHOPBOX_REFRESH_TOKEN', '')
    )
    # get_all_payments(sdk)
    # get(sdk)
    create(sdk)


if __name__ == "__main__":
    main()
