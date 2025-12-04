"""Payments API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class PaymentsAPI(BaseAPI):
    """Handle product-related operations"""

    def get_all(self, page: int = 1, **filters) -> Dict:
        """Fetch all products with optional filters."""
        url = f"{self.base_url}/payments/api/v1/payout"
        return self._make_request("GET", url)

    def get(self, params: Dict) -> Dict:
        """Fetch a single product by SKU."""
        url = f"{self.eshopbox_url}/payments/api/v1/payout"
        return self._make_request("GET", url, params=params)

    def create(self, payload: Dict) -> Dict:
        """Create a new product."""
        url = f"{self.eshopbox_url}/payments/api/v1/payout"
        return self._make_request("POST", url, json=payload)
