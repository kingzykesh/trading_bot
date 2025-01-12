# Rust Crypto Trading Bot

This project is a cryptocurrency trading bot built in Python. It fetches real-time price data from the CoinMarketCap API and uses a simple trading strategy based on predefined buy and sell price thresholds. The bot is designed to automate cryptocurrency trading and can be further extended to integrate with popular cryptocurrency exchanges like Binance or Huobi.

## Features

- **Real-Time Price Tracking**: Fetches the latest cryptocurrency prices using the CoinMarketCap API.
- **Customizable Strategy**: Implements a simple trading strategy with configurable buy and sell thresholds.
- **Automated Monitoring**: Continuously monitors the market with a user-defined time interval.
- **Error Handling**: Handles API errors and network issues gracefully.
- **Extensibility**: Ready to integrate with cryptocurrency exchange APIs for live trading.

## Requirements

- Python 3.7+
- CoinMarketCap API key (Free or paid API key required)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/crypto-trading-bot.git
   cd crypto-trading-bot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables (recommended):
   ```bash
   export COINMARKETCAP_API_KEY="your_api_key"
   ```

## Usage

1. Configure the trading parameters in the `crypto_bot.py` file:
   - **Symbol**: Cryptocurrency symbol (e.g., BTC, ETH).
   - **Buy Price**: Price threshold to trigger a buy.
   - **Sell Price**: Price threshold to trigger a sell.

2. Run the bot:
   ```bash
   python crypto_bot.py
   ```

3. Monitor the console for real-time updates:
   - Fetches the latest prices.
   - Prints buy, sell, or hold signals based on the strategy.

## Example Output

```plaintext
Fetching latest price...
Current BTC price: $35000.12
[BUY SIGNAL] Current price ($35000.12) is below or equal to buy price ($35000.0).

Fetching latest price...
Current BTC price: $40000.89
[SELL SIGNAL] Current price ($40000.89) is above or equal to sell price ($40000.0).
```

## Extending the Bot

- **Integration with Exchanges**: Use APIs from Binance, Huobi, or other platforms to execute real trades.
- **Advanced Strategies**: Implement more sophisticated strategies such as moving averages, RSI, or machine learning models.
- **Notifications**: Add email, SMS, or Telegram notifications for buy/sell signals.

## Project Structure

```plaintext
crypto-trading-bot/
├── crypto_bot.py         # Main bot script
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Dependencies

- `requests`: For making HTTP requests to the CoinMarketCap API.
- `urllib3`: For handling retries and connection pooling.

Install all dependencies using:
```bash
pip install -r requirements.txt
```

## Known Issues

- **Network Errors**: Ensure stable internet connectivity for uninterrupted operation.
- **API Rate Limits**: CoinMarketCap free-tier users may encounter rate limits. Upgrade the API plan if necessary.

## Disclaimer

This bot is for educational purposes only. Cryptocurrency trading is highly volatile and involves significant risk. Use this bot at your own discretion and responsibility.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements or features.

---

### Author

Ezirim Kingdom   
https://ezirimkingdom.com.ng

