from __future__ import annotations

import datetime
from typing import Dict, Tuple, List

from frankfurter import (
    get_currencies as ff_get_currencies,
    get_latest_rate as ff_get_latest_rate,
    get_historical_rate as ff_get_historical_rate,
    get_rate_trend as ff_get_rate_trend,
)


def fetch_currencies() -> Dict[str, str]:
    """Return mapping of currency codes to names."""
    return ff_get_currencies()


def list_currency_codes() -> List[str]:
    """Return sorted list of available currency codes."""
    currencies = fetch_currencies()
    return sorted(currencies.keys())


def _extract_rate_or_raise(payload: Dict, to_currency: str) -> Tuple[str, float]:
    """Extract (date, rate) from Frankfurter payload.

    Handles the two common shapes:
    - Latest/Historical single-date: {"date": "YYYY-MM-DD", "rates": {TO: rate}}
    - Range: {"rates": {"YYYY-MM-DD": {TO: rate}, ...}}
    """
    if not isinstance(payload, dict) or "rates" not in payload:
        raise ValueError("Malformed response: 'rates' not found")

    rates = payload["rates"]

    # Range payload
    if isinstance(rates, dict) and rates and isinstance(next(iter(rates.values())), dict):
        # pick chronologically sorted dates
        date_keys = sorted(rates.keys())
        last_date = date_keys[-1]
        day_rates = rates[last_date]
        if to_currency not in day_rates:
            raise ValueError(f"Target currency '{to_currency}' not in rates for {last_date}")
        return last_date, float(day_rates[to_currency])

    # Single-date payload
    if "date" not in payload:
        raise ValueError("Malformed response: 'date' not found for single-date payload")
    date = payload["date"]
    if to_currency not in rates:
        raise ValueError(f"Target currency '{to_currency}' not in rates")
    return date, float(rates[to_currency])


def latest_rate(from_currency: str, to_currency: str) -> Tuple[str, float]:
    """Return (date, rate) for the most recent conversion rate."""
    payload = ff_get_latest_rate(from_currency, to_currency)
    return _extract_rate_or_raise(payload, to_currency)


def historical_rate(date: str, from_currency: str, to_currency: str) -> Tuple[str, float]:
    """Return (date, rate) for a specific date."""
    payload = ff_get_historical_rate(date, from_currency, to_currency)
    return _extract_rate_or_raise(payload, to_currency)


def rate_trend_last_3y(from_currency: str, to_currency: str) -> Dict[str, float]:
    """Return mapping {date: rate} from 3 years ago to today."""
    start_date = (datetime.date.today() - datetime.timedelta(days=365 * 3)).isoformat()
    payload = ff_get_rate_trend(start_date, from_currency, to_currency)

    # Expect payload shape: {"rates": {"YYYY-MM-DD": {TO: rate}, ...}}
    if "rates" not in payload or not isinstance(payload["rates"], dict):
        raise ValueError("Malformed response: 'rates' not found for trend data")

    trend: Dict[str, float] = {}
    for date_str, day_rates in payload["rates"].items():
        if to_currency in day_rates:
            trend[date_str] = float(day_rates[to_currency])

    # Sort by date for deterministic order
    return dict(sorted(trend.items(), key=lambda kv: kv[0]))


def compute_inverse(rate: float) -> float:
    if rate == 0:
        raise ValueError("Rate cannot be zero for inverse computation")
    return 1.0 / rate
