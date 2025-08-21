import os
from dotenv import load_dotenv

# Load environment variables from the .env file in the project root
load_dotenv()

# --- API Credentials ---
# Fetches the keys from the environment. Raises an error if a key is missing.
try:
    CONSUMER_KEY = os.environ["TRADEME_CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["TRADEME_CONSUMER_SECRET"]
    OAUTH_TOKEN = os.environ["TRADEME_OAUTH_TOKEN"]
    OAUTH_TOKEN_SECRET = os.environ["TRADEME_OAUTH_TOKEN_SECRET"]
except KeyError as e:
    raise RuntimeError(f"Missing required environment variable: {e}. Please check your .env file.") from e

# --- API URL ---
BASE_API_URL = "https://api.tmsandbox.co.nz/v1"