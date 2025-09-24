# FX Converter Web App

🌐 **Live Demo**: [https://app-currency-converter-dsp.streamlit.app/](https://app-currency-converter-dsp.streamlit.app/)

## My Details
- **Full Name:** WAI WING TANG
- **Student ID:** 25132527

## Project Description
A web application built with Python and Streamlit that allows users to perform currency conversions using real-time and historical data from the Frankfurter API. It can display the latest rates, historical rates, and show a trend over the last three years.

## Features
- 💱 Real-time currency conversion with live exchange rates
- 📅 Historical exchange rates for specific dates
- 📈 Interactive 3-year trend chart with proper axis labels
- 🌍 Support for multiple currencies via Frankfurter API
- 📱 Responsive web interface built with Streamlit

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

## Quick Start
### Try the Live App
Visit the deployed application: [https://app-currency-converter-dsp.streamlit.app/](https://app-currency-converter-dsp.streamlit.app/)

### Run Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com/BirdUTS/streamlit-currency-converter.git
   cd streamlit-currency-converter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser** and navigate to `http://localhost:8501`

## Usage
1. **Enter Amount**: Specify the amount you want to convert
2. **Select Currencies**: Choose from and to currencies from the dropdown menus
3. **Get Latest Rate**: Click to see current exchange rate and 3-year trend chart
4. **Historical Rates**: Select a specific date and click "Conversion Rate" for historical data

## Technology Stack
- **Frontend**: Streamlit
- **Data Visualization**: Altair
- **API**: Frankfurter API (European Central Bank data)
- **Data Processing**: Pandas
- **HTTP Requests**: Requests library
