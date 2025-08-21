import pytest
from trademe_automation.api_client.trademe_client import TradeMeClient

@pytest.fixture(scope="session")
def api_client():
    """Provides an authenticated TradeMe API client for the entire test session."""
    client = TradeMeClient()
    yield client