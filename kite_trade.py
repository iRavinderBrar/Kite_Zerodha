import os
import requests


class KiteApp:
    def __init__(self, authorization):
        self.headers = {"Authorization": authorization}
        self.session = requests.session()
        self.root_url = "https://kite.zerodha.com/oms"
        self.session.get(self.root_url, headers=self.headers)

    def profile(self):
        profile = self.session.get(f"{self.root_url}/user/profile", headers=self.headers).json()["data"]
        return profile

    def orders(self):
        orders = self.session.get(f"{self.root_url}/orders", headers=self.headers).json()["data"]
        return orders

    def positions(self):
        positions = self.session.get(f"{self.root_url}/portfolio/positions", headers=self.headers).json()["data"]
        return positions

    def place_order(self, variety, exchange, tradingsymbol, transaction_type, quantity, product, order_type, price=None,
                    validity=None, validity_ttl=None, disclosed_quantity=None, trigger_price=None, iceberg_legs=None,
                    iceberg_quantity=None, auction_number=None, tag=None, market_protection=None):
        params = locals()
        del params["self"]
        for k in list(params.keys()):
            if params[k] is None:
                del params[k]
        order_id = self.session.post(f"{self.root_url}/orders/{variety}", data=params,
                                     headers=self.headers).json()["data"]["order_id"]
        return order_id

    def modify_order(self, variety, order_id, parent_order_id=None, quantity=None, price=None, order_type=None,
                     trigger_price=None, validity=None, disclosed_quantity=None, market_protection=None):
        params = locals()
        del params["self"]
        for k in list(params.keys()):
            if params[k] is None:
                del params[k]

        order_id = self.session.put(f"{self.root_url}/orders/{variety}/{order_id}", data=params,
                                    headers=self.headers).json()["data"]["order_id"]
        return order_id

    def cancel_order(self, variety, order_id, parent_order_id=None):
        order_id = self.session.delete(f"{self.root_url}/orders/{variety}/{order_id}",
                                       data={"parent_order_id": parent_order_id} if parent_order_id else {},
                                       headers=self.headers).json()["data"]["order_id"]
        return order_id

