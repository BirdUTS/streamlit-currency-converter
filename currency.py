from __future__ import annotations


def _format_amount(value: float, decimals: int) -> str:
    return f"{value:,.{decimals}f}"


def format_conversion_result(date: str, from_currency: str, to_currency: str, rate: float, from_amount: float) -> str:
    """Return a human-friendly conversion summary string.

    - to_amount = from_amount * rate
    - inverse_rate = 1 / rate
    - Rates formatted to 4 decimals, amounts to 2 decimals
    """
    to_amount = from_amount * rate if from_amount is not None else 0.0
    inverse_rate = 1.0 / rate if rate not in (0, None) else 0.0

    rate_str = _format_amount(rate, 4)
    inverse_rate_str = _format_amount(inverse_rate, 4)
    from_amount_str = _format_amount(from_amount, 2)
    to_amount_str = _format_amount(to_amount, 2)

    return (
        f"The conversion rate on {date} from {from_currency} to {to_currency} was {rate_str}. "
        f"So {from_amount_str} in {from_currency} correspond to {to_amount_str} in {to_currency}. "
        f"The inverse rate was {inverse_rate_str}."
    )
