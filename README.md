
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
                  
```
