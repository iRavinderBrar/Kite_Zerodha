
# Python Code for Kite Zerodha Platform

* __Author: [AlgoTrader](https://www.youtube.com/@iRavinderBrar)__

## Installation

How to use:

```
# Download the 'kite_trade.py' file
# keep the file in same directory where your code file is stored
```

### Prerequisites

Python >=3.7

### Python Code Example
Import
```python

from kite_trade import *

```
Log In Method
```python
# # Provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'AlgoTrader'

enctoken = ""
kite = KiteApp(enctoken=enctoken)
```

Basic API Calls
```python
# Basic calls
print(kite.profile())
print(kite.margins())
print(kite.orders())
print(kite.positions())

# Get instrument or exchange
print(kite.instruments())
print(kite.instruments("NSE"))
print(kite.instruments("NFO"))
```

Get Tick Data 'Use Websocket'
```python
from kiteconnect import KiteTicker
user_id = kite.profile()["user_id"]
kws = KiteTicker(api_key="AlgoTrader", access_token=enctoken+"&user_id="+user_id)

def on_ticks(ws, ticks):
    print(ticks)

kws.on_ticks = on_ticks
kws.connect(threaded=True)
while not kws.is_connected():
    time.sleep(1)
print("WebSocket : Connected")
# use instrument_token to get data
kws.subscribe([256265, 260105, 738561, 5633])
kws.set_mode(kws.MODE_QUOTE, [256265, 260105, 738561, 5633])
time.sleep(30)
kws.unsubscribe([256265, 260105, 738561, 5633])
```

Get Historical Data
```python
import datetime
instrument_token = 9604354
from_datetime = datetime.datetime.now() - datetime.timedelta(days=7)     # From last & days
to_datetime = datetime.datetime.now()
interval = "5minute"
print(kite.historical_data(instrument_token, from_datetime, to_datetime, interval, continuous=False, oi=False))
```

Place Order
```python
order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="ACC",
                         transaction_type=kite.TRANSACTION_TYPE_BUY,
                         quantity=1,
                         product=kite.PRODUCT_MIS,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="AlgoTrader")

print(order)
```

Modify order
```python
kite.modify_order(variety=kite.VARIETY_REGULAR,
                  order_id="order_id",
                  parent_order_id=None,
                  quantity=5,
                  price=200,
                  order_type=kite.ORDER_TYPE_LIMIT,
                  trigger_price=None,
                  validity=kite.VALIDITY_DAY,
                  disclosed_quantity=None)

```

Cancel order
```python
kite.cancel_order(variety=kite.VARIETY_REGULAR,
                  order_id="order_id",
                  parent_order_id=None)
```
                  
Get All GTT Orders
```python
gtt_orders():
```

Get a specific GTT Order by OrderId
```python
gtt_order(order_id):
```

Delete a specific GTT Order by OrderId
```python
gtt_delete_order(order_id):
```

Create a GTT Order
```python
gtt_create_order(self, exchange, tradingsymbol, transaction_type, order_type, product, trigger_type, last_price, quantity, price_values, trigger_values):

# Sample of Single Leg Sell GTT Order
kite.gtt_create_order('NSE', 'HDFCBANK', 'SELL', 'LIMIT', 'CNC', 'single', 1810.25, 10, [1840.5], [1840])

# Sample of Single Leg Buy GTT Order
kite.gtt_create_order('NSE', 'HDFCBANK', 'BUY', 'LIMIT', 'CNC', 'single', 1810.25, 10, [1820.5], [1818])

# Sample of Two Leg GTT Order - OCO
kite.gtt_create_order('NSE', 'HDFCBANK', 'SELL', 'LIMIT', 'CNC', 'two-leg', 1810.25, 10, [1780, 1840], [1782, 1838])

```
