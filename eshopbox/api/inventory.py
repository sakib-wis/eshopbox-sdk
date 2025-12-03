"""Inventory API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class InventoryAPI(BaseAPI):
    """Handle inventory-related operations"""

    def get_all(self, sku: str = None) -> Dict:
        """Get inventory for all or specific SKU."""
        url = f"{self.base_url}/api/v1/inventory"
        params = {"sku": sku} if sku else {}
        return self._make_request("GET", url, params=params)

    def update(self, inventory_data: Dict) -> Dict:
        """Update inventory levels."""
        url = f"{self.eshopbox_url}/api/inventory/update"
        return self._make_request("POST", url, json=inventory_data)
