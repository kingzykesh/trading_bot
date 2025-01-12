import os
import requests
import time

# Set up environment variables for secure API key management
COINMARKETCAP_API_KEY = "1db749ff-b388-4718-86ec-83555ef909d8"

# Base URL for CoinMarketCap API
BASE_URL = "https://pro-api.coinmarketcap.com/v1"

# Headers for CoinMarketCap API requests
HEADERS = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': COINMARKETCAP_API_KEY,
}

def fetch_latest_price(symbol: str, convert: str = "USD") -> float:
    """Fetch the latest price of a cryptocurrency from CoinMarketCap."""
    url = f"{BASE_URL}/cryptocurrency/quotes/latest"
    parameters = {
        'symbol': symbol,
        'convert': convert
    }
    try:
        response = requests.get(url, headers=HEADERS, params=parameters)
        response.raise_for_status()
        data = response.json()
        price = data['data'][symbol]['quote'][convert]['price']
        return price
    except Exception as e:
        print(f"Error fetching price for {symbol}: {e}")
        return 0.0

def trading_strategy(current_price: float, buy_price: float, sell_price: float):
    """Example trading strategy based on price thresholds."""
    if current_price <= buy_price:
        print(f"[BUY SIGNAL] Current price (${current_price}) is below or equal to buy price (${buy_price}).")
        # Trigger a buy action (placeholder for API integration with an exchange)
        # Example: execute_trade('BUY', amount, current_price)
    elif current_price >= sell_price:
        print(f"[SELL SIGNAL] Current price (${current_price}) is above or equal to sell price (${sell_price}).")
        # Trigger a sell action (placeholder for API integration with an exchange)
        # Example: execute_trade('SELL', amount, current_price)
    else:
        print(f"[HOLD] Current price (${current_price}) does not meet buy or sell conditions.")

def main():
    """Main function to run the trading bot."""
    symbol = "BTC"  # Cryptocurrency symbol
    buy_price = 35000.0  # Example buy price threshold in USD
    sell_price = 40000.0  # Example sell price threshold in USD

    while True:
        print("\nFetching latest price...")
        current_price = fetch_latest_price(symbol)
        if current_price:
            print(f"Current {symbol} price: ${current_price:.2f}")
            trading_strategy(current_price, buy_price, sell_price)
        else:
            print("Unable to retrieve the price. Retrying...")
        
        time.sleep(60)  # Pause for 60 seconds before checking again

if __name__ == "__main__":
    main()
