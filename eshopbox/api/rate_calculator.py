"""Rate Calculator API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class RateCalculatorAPI(BaseAPI):
    """Calculate shipping rates"""

    def calculate(self, rate_data: Dict) -> Dict:
        """Calculate shipping rate."""
        url = f"{self.eshopbox_url}/api/rate-calculator"
        return self._make_request("POST", url, json=rate_data)
