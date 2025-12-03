"""RateCalculator API module"""

from typing import Dict, Optional, List
from eshopbox.api.base import BaseAPI


class RateCalculatorAPI(BaseAPI):
    """Handle order-related operations"""

    def get_all(self, page: int = 1, **filters) -> Dict:
        """
        Get all rate-calculator with optional filters

        Args:
            page: Page number for pagination
            **filters: Additional filter parameters

        Returns:
            Dict containing order data
        """
        url = f"{self.base_url}/api/v1/rate-calculator/erp"
        params = {"filters": f"page={page}"}
        params.update(filters)
        return self._make_request("GET", url, params=params)
