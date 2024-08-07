
import os
import json
from dotenv import load_dotenv
from unstructured_client import UnstructuredClient
from unstructured_client.models import shared
from unstructured_client.models.errors import SDKError


def load_config():
    """Load environment variables for API configuration."""
    load_dotenv()
    api_key = os.getenv('UNSTRUCTURED_API')
    unstructured_url = os.getenv('UNSTRUCTURED_URL')
    return api_key, unstructured_url

print(load_config())
