# FX Converter Web App

## My Details
- **Full Name:** [Your Name]
- **Student ID:** [Your Student ID]

## Project Description
A web application built with Python and Streamlit that allows users to perform currency conversions using real-time and historical data from the Frankfurter API. It can display the latest rates, historical rates, and show a trend over the last three years.

## Python Functions
- **frankfurter.py**:
  - `get_currencies()`: Fetch the mapping of currency codes to names from the Frankfurter API.
  - `get_latest_rate(from_currency, to_currency)`: Get the latest rate JSON between two currencies.
  - `get_historical_rate(date, from_currency, to_currency)`: Get the rate JSON for a specific date.
  - `get_rate_trend(start_date, from_currency, to_currency)`: Get range JSON for historical rates from a start date up to today.

- **api.py**:
  - `fetch_currencies()`: Return the mapping of currencies.
  - `list_currency_codes()`: Return a sorted list of available currency codes.
  - `latest_rate(from_currency, to_currency)`: Return `(date, rate)` for the most recent rate.
  - `historical_rate(date, from_currency, to_currency)`: Return `(date, rate)` for a given date.
  - `rate_trend_last_3y(from_currency, to_currency)`: Return a `{date: rate}` mapping for the last 3 years.
  - `compute_inverse(rate)`: Helper to compute an inverse rate safely.

- **currency.py**:
  - `format_conversion_result(date, from_currency, to_currency, rate, from_amount)`: Format a human-friendly summary string including the converted amount and inverse rate.

## Instructions for Running
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```
