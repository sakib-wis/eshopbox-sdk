"""Products API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class ProductsAPI(BaseAPI):
    """Handle product-related operations"""

    def get_all(self, page: int = 1, **filters) -> Dict:
        """Fetch all products with optional filters."""
        url = f"{self.base_url}/api/v1/products"
        params = {"filters": f"page={page}"}
        params.update(filters)
        return self._make_request("GET", url, params=params)

    def get(self, sku: str) -> Dict:
        """Fetch a single product by SKU."""
        url = f"{self.eshopbox_url}/api/product/{sku}"
        return self._make_request("GET", url)

    def create(self, product_data: Dict) -> Dict:
        """Create a new product."""
        url = f"{self.eshopbox_url}/api/product"
        return self._make_request("POST", url, json=product_data)

    def update(self, sku: str, product_data: Dict) -> Dict:
        """Update an existing product."""
        url = f"{self.eshopbox_url}/api/product/{sku}"
        return self._make_request("PUT", url, json=product_data)
