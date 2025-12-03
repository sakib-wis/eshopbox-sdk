"""Shipments API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class ShipmentsAPI(BaseAPI):
    """Handle shipment-related operations"""

    def get_all(self, page: int = 1) -> Dict:
        """Get all shipments."""
        url = f"{self.base_url}/api/v1/shipments"
        params = {"page": page}
        return self._make_request("GET", url, params=params)

    def track(self, awb_number: str) -> Dict:
        """Track shipment by AWB number."""
        url = f"{self.eshopbox_url}/api/track/{awb_number}"
        return self._make_request("GET", url)

    def generate_shipping_label(self, shipment_id: str) -> Dict:
        """Generate shipping label for a shipment."""
        url = f"{self.eshopbox_url}/api/shipment/{shipment_id}/label"
        return self._make_request("GET", url)

    def cancel(self, shipment_id: str) -> Dict:
        """Cancel a shipment."""
        url = f"{self.eshopbox_url}/api/shipment/{shipment_id}/cancel"
        return self._make_request("POST", url)
