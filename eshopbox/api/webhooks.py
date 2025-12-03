"""Webhooks API module"""

from typing import Dict
from eshopbox.api.base import BaseAPI


class WebhooksAPI(BaseAPI):
    """Manage webhooks"""

    def list(self) -> Dict:
        """List all registered webhooks."""
        url = f"{self.eshopbox_url}/api/webhooks"
        return self._make_request("GET", url)

    def create(self, webhook_data: Dict) -> Dict:
        """Create a webhook."""
        url = f"{self.eshopbox_url}/api/webhook"
        return self._make_request("POST", url, json=webhook_data)

    def delete(self, webhook_id: str) -> Dict:
        """Delete a webhook."""
        url = f"{self.eshopbox_url}/api/webhook/{webhook_id}"
        return self._make_request("DELETE", url)
