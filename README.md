# Binance Futures Tradebot Version 2

This trade bot utilizes Binance Futures API to access Binance websocket, creating new orders and take profit based on filled orders. 

## Features
- Roughly 5% ROE a day per symbol
- Sending trade/pnl info using Telegram
- Can run forever
- Customize input based on risk appetite

## WIP
- Interact with the script using Telegram or on Web
- Fully auto (auto choosing input based on market ticker)
- Run on multiple users

## Usage:

1. Get your API Key/Secret from Binance(enable Future) and TOKEN/chat_id from Telegram Bot Father: <br />

    Binance: https://www.binance.com/en/my/settings/api-management <br />
    Telegram (Optional): https://telegram.me/BotFather <br />

2. Add them to a dotenv(.env) file: <br />

   ```javascript
   API_KEY = ""
   API_SECRET = ""
   TOKEN = ""
   chat_id = ""
   ```

3. Install all the package in requirements.txt: <br />

   ```console
   pip install -r requirements.txt
   ```

4. Run main.py: <br />
   ```console
   python main.py
   ```
