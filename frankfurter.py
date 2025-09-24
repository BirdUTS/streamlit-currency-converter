import datetime
from typing import Dict, Any

import requests

BASE_URL = "https://api.frankfurter.app"
DEFAULT_TIMEOUT_SECONDS = 15


def _get(url: str, params: Dict[str, Any] | None = None) -> Dict[str, Any]:
    response = requests.get(url, params=params, timeout=DEFAULT_TIMEOUT_SECONDS)
    response.raise_for_status()
    return response.json()


def get_currencies() -> Dict[str, str]:
    """Fetch all available currency codes and their names.

    Returns:
        Mapping like {"AUD": "Australian Dollar", ...}
    """
    url = f"{BASE_URL}/currencies"
    data = _get(url)
    return data


def get_latest_rate(from_currency: str, to_currency: str) -> Dict[str, Any]:
    """Get the most recent conversion rate between two currencies.

    Args:
        from_currency: Source currency code, e.g., "AUD".
        to_currency: Target currency code, e.g., "USD".

    Returns:
        Raw JSON response from the API as a dictionary.
    """
    url = f"{BASE_URL}/latest"
    params = {"from": from_currency, "to": to_currency}
    return _get(url, params=params)


def get_historical_rate(date: str, from_currency: str, to_currency: str) -> Dict[str, Any]:
    """Get the conversion rate for a specific date.

    Args:
        date: Date in 'YYYY-MM-DD' format.
        from_currency: Source currency code.
        to_currency: Target currency code.

    Returns:
        Raw JSON response from the API as a dictionary.
    """
    url = f"{BASE_URL}/{date}"
    params = {"from": from_currency, "to": to_currency}
    return _get(url, params=params)


def get_rate_trend(start_date: str, from_currency: str, to_currency: str) -> Dict[str, Any]:
    """Get historical rate data from a start date until today for trend charts.

    Args:
        start_date: Start date in 'YYYY-MM-DD' format (e.g., three years ago).
        from_currency: Source currency code.
        to_currency: Target currency code.

    Returns:
        Raw JSON response from the API as a dictionary.
    """
    end_date = datetime.date.today().isoformat()
    url = f"{BASE_URL}/{start_date}..{end_date}"
    params = {"from": from_currency, "to": to_currency}
    return _get(url, params=params)
