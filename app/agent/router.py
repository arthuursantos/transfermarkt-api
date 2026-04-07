import logging
import os

from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

logger = logging.getLogger(__name__)

def routerModel(model: str):
    load_dotenv()
    _api_key = os.getenv("OPENROUTER_API_KEY")
    _base_url = os.getenv("OPENROUTER_BASE_URL")
    if _api_key is None or _base_url is None:
        raise EnvironmentError("OPENROUTER_API_KEY and OPENROUTER_BASE_URL must be set in the environment variables.")
    logger.info("Initializing LiteLlm model=%s, api_base=%s, api_key=%s...", model, _base_url, _api_key[:8] + "***")
    return LiteLlm(
        model=model,
        api_key=_api_key,
        api_base=_base_url
    )