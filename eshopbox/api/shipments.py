"""Shipments API module"""

from typing import Dict, Optional
from eshopbox.api.base import BaseAPI


class ShipmentsAPI(BaseAPI):
    """Handle shipment-related operations"""
    
    def get_all(self, **filters) -> Dict:
        """
        Get all shipments with optional filters
        
        Args:
            **filters: Filter parameters
            
        Returns:
            Dict containing shipment data
        """
        url = f"{self.eshopbox_url}/api/order/shipment"
        return self._make_request("GET", url, params=filters)
    
    def get(self, external_shipment_id: str) -> Dict:
        """
        Get a specific shipment
        
        Args:
            external_shipment_id: Shipment identifier
            
        Returns:
            Dict containing shipment details
        """
        url = f"{self.eshopbox_url}/api/order/shipment/{external_shipment_id}"
        return self._make_request("GET", url)
    
    def create(self, shipment_data: Dict) -> Dict:
        """
        Create a new shipment
        
        Args:
            shipment_data: Shipment information
            
        Returns:
            Dict containing created shipment details
        """
        url = f"{self.eshopbox_url}/api/order/shipment"
        return self._make_request("POST", url, json=shipment_data)
    
    def update_status(self, external_shipment_id: str, status: str) -> Dict:
        """
        Update shipment status
        
        Args:
            external_shipment_id: Shipment identifier
            status: New status (e.g., 'delivered', 'shipped')
            
        Returns:
            Dict containing status update confirmation
        """
        url = f"{self.eshopbox_url}/api/order/shipment/{external_shipment_id}/mark{status}"
        return self._make_request("PUT", url)
    
    def get_tracking_details(self, tracking_ids: str) -> Dict:
        """
        Get tracking details via polling
        
        Args:
            tracking_ids: Comma-separated tracking IDs
            
        Returns:
            Dict containing tracking information
        """
        url = f"{self.eshopbox_url}/api/v1/shipping/trackingDetails"
        params = {"trackingIds": tracking_ids}
        return self._make_request("GET", url, params=params)
    
    def cancel_tracking(self, tracking_data: Dict) -> Dict:
        """
        Cancel shipment tracking
        
        Args:
            tracking_data: Tracking cancellation information
            
        Returns:
            Dict containing cancellation confirmation
        """
        url = f"{self.eshopbox_url}/api/v1/shipping/cancel"
        return self._make_request("POST", url, json=tracking_data)
