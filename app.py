from __future__ import annotations

import datetime

import pandas as pd
import streamlit as st
import altair as alt

from api import (
    list_currency_codes,
    latest_rate,
    historical_rate,
    rate_trend_last_3y,
)
from currency import format_conversion_result


st.title("FX Converter")

# Inputs
amount = st.number_input("Enter the amount to be converted:", value=50.0)

# Fetch currencies
try:
    currency_codes = list_currency_codes()
except Exception as e:
    st.error(f"Failed to fetch currencies: {e}")
    st.stop()

# Defaults for convenience
default_from = "AUD" if "AUD" in currency_codes else currency_codes[0]
default_to = "USD" if "USD" in currency_codes else (currency_codes[1] if len(currency_codes) > 1 else currency_codes[0])

col1, col2 = st.columns(2)
with col1:
    from_currency = st.selectbox("From Currency", currency_codes, index=currency_codes.index(default_from))
with col2:
    to_currency = st.selectbox("To Currency", currency_codes, index=currency_codes.index(default_to))

latest_btn = st.button("Get Latest Rate")

hist_date = st.date_input("Select a date for historical rates:", value=datetime.date.today())
convert_btn = st.button("Conversion Rate")

# Latest rate flow
if latest_btn:
    try:
        rate_date, rate_value = latest_rate(from_currency, to_currency)
        result_text = format_conversion_result(rate_date, from_currency, to_currency, rate_value, amount)
        st.write(result_text)

        st.subheader("Rate Trend Over the Last 3 years")
        trend = rate_trend_last_3y(from_currency, to_currency)
        if not trend:
            st.info("No trend data available.")
        else:
            df = pd.DataFrame({"date": list(trend.keys()), "rate": list(trend.values())})
            df["date"] = pd.to_datetime(df["date"])  # ensure proper temporal axis
            chart = (
                alt.Chart(df)
                .mark_line()
                .encode(
                    x=alt.X("date:T", title="Date", axis=alt.Axis(labelAngle=0)),
                    y=alt.Y("rate:Q", title="Rate"),
                    tooltip=[alt.Tooltip("date:T", title="Date"), alt.Tooltip("rate:Q", title="Rate", format=".4f")],
                )
                .properties(height=320)
            )
            st.altair_chart(chart, use_container_width=True)
    except Exception as e:
        st.error(f"Failed to fetch latest rate or trend: {e}")

# Historical conversion flow
if convert_btn:
    try:
        date_str = hist_date.isoformat() if isinstance(hist_date, datetime.date) else str(hist_date)
        rate_date, rate_value = historical_rate(date_str, from_currency, to_currency)
        result_text = format_conversion_result(rate_date, from_currency, to_currency, rate_value, amount)
        st.write(result_text)
    except Exception as e:
        st.error(f"Failed to fetch historical rate: {e}")
