from requests_oauthlib import OAuth1Session
from trademe_automation.config import settings

class TradeMeClient:
    """A client to interact with the TradeMe Sandbox API."""

    def __init__(self):
        """Initializes the client with OAuth1 credentials from settings."""
        self.session = OAuth1Session(
            client_key=settings.CONSUMER_KEY,
            client_secret=settings.CONSUMER_SECRET,
            resource_owner_key=settings.OAUTH_TOKEN,
            resource_owner_secret=settings.OAUTH_TOKEN_SECRET
        )
        self.base_url = settings.BASE_API_URL

    def get_latest_listings(self):
        """
        Retrieves the latest listings.
        Corresponds to: GET /v1/Listings/Latest.json
        """
        url = f"{self.base_url}/Listings/Latest.json"
        return self.session.get(url)

    def list_item(self, payload: dict):
        """
        Lists an item for sale.
        Corresponds to: POST /v1/Selling.json
        """
        url = f"{self.base_url}/Selling.json"
        headers = {'Content-Type': 'application/json'}
        return self.session.post(url, headers=headers, json=payload)