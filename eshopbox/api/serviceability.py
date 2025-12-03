"""Serviceability API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class ServiceabilityAPI(BaseAPI):
    """Check whether a PIN code or region is serviceable"""

    def check_pincode(self, pincode: str) -> Dict:
        """Check serviceability for a PIN code."""
        url = f"{self.eshopbox_url}/api/serviceability/{pincode}"
        return self._make_request("GET", url)

    def check_address(self, address_data: Dict) -> Dict:
        """Check serviceability for full address."""
        url = f"{self.eshopbox_url}/api/serviceability/address"
        return self._make_request("POST", url, json=address_data)
