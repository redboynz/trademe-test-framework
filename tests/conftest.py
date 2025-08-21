import sys
import os
import pytest

# --- Start of Path Modification ---
# This block manually adds your 'src' directory to the list of places
# Python looks for modules. This is a direct fix for import errors.

# Get the absolute path to the directory containing this file (tests/)
current_dir = os.path.dirname(__file__)
# Go one level up to the project root and then into the 'src' folder
src_path = os.path.abspath(os.path.join(current_dir, '..', 'src'))
# Add this path to the beginning of the system path
sys.path.insert(0, src_path)
# --- End of Path Modification ---


# Now, the original import statement should work correctly
from trademe_automation.api_client.trademe_client import TradeMeClient


@pytest.fixture(scope="session")
def api_client():
    """Provides an authenticated TradeMe API client for the entire test session."""
    client = TradeMeClient()
    yield client