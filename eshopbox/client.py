"""Main SDK client for EShopBox"""

from eshopbox.auth import EShopBoxAuth
from eshopbox.api.orders import OrdersAPI
from eshopbox.api.consignments import ConsignmentsAPI
from eshopbox.api.inventory import InventoryAPI
from eshopbox.api.products import ProductsAPI
from eshopbox.api.rate_calculator import RateCalculatorAPI
from eshopbox.api.returns import ReturnsAPI
from eshopbox.api.serviceability import ServiceabilityAPI
from eshopbox.api.shipments import ShipmentsAPI
from eshopbox.api.webhooks import WebhooksAPI
# Import other API modules...


class EShopBoxSDK:
    """
    Main SDK class for EShopBox API

    Example:
        >>> sdk = EShopBoxSDK(
        ...     workspace="myshop",
        ...     client_id="client_id",
        ...     client_secret="secret",
        ...     refresh_token="token"
        ... )
        >>> orders = sdk.orders.get_all()
    """

    def __init__(
        self,
        workspace: str,
        client_id: str,
        client_secret: str,
        refresh_token: str
    ):
        """
        Initialize EShopBox SDK

        Args:
            workspace: Your EShopBox workspace name
            client_id: Your API client ID
            client_secret: Your API client secret
            refresh_token: Your API refresh token
        """
        self.workspace = workspace
        self.auth = EShopBoxAuth(client_id, client_secret, refresh_token)

        # Initialize API modules
        self.orders = OrdersAPI(workspace, self.auth)
        self.consignments = ConsignmentsAPI(workspace, self.auth)
        self.inventory = InventoryAPI(workspace, self.auth)
        self.products = ProductsAPI(workspace, self.auth)
        self.rate_calculator = RateCalculatorAPI(workspace, self.auth)
        self.returns = ReturnsAPI(workspace, self.auth)
        self.serviceability = ServiceabilityAPI(workspace, self.auth)
        self.shipments = ShipmentsAPI(workspace, self.auth)
        self.webhooks = WebhooksAPI(workspace, self.auth)
