
# Python Code for Kite Zerodha Platform

* __Author: [AlgoTrader](https://www.youtube.com/@iRavinderBrar)__

How to use:

* __Video: [AlgoTrader](https://youtu.be/MWtgtUkhT9A)__

### Prerequisites

Python >=3.7

### Python Code Example
Import
```python

# # Get the code from above kite.trade.py file

```
Log In Method
```python
# # Provide 'authorization' token manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window

authorization = ""
kite = KiteApp(authorization=authorization)
```

Basic API Calls
```python
# Basic calls
print(kite.profile())
print(kite.orders())
```
# Basic Order Placement
Place Order
```python
order = kite.place_order(variety="regular",
                         exchange="NSE",
                         tradingsymbol="ACC",
                         transaction_type="BUY",
                         quantity=1,
                         product="MIS",
                         order_type="MARKET"
                         tag="AlgoTrader")

print(order)
```

Modify order
```python
kite.modify_order(variety="regular",
                  order_id="order_id",
                  quantity=5,
                  price=200)
print(order)
```

Cancel order
```python
kite.cancel_order(variety="regular",
                  order_id="order_id")
print(order)
```
                  
```
