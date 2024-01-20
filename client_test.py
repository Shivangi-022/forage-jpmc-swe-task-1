import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for i in quotes:
      self.assertEqual(getDataPoint(i),( i['stock'], i['bid_price'], i['ask_price'], (i['bid_price'] + i['ask_price'])/2 ))
  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for i in quotes:
      stock, bid_price, ask_price, price = getDataPoint(i)
      self.assertEqual(stock, i['stock'])
      self.assertEqual(bid_price, float(i['top_bid']['price']))
      self.assertEqual(ask_price, float(i['top_ask']['price']))
      price_a = float(i['top_bid']['price'])
      price_b = float(i['top_ask']['price'])
      # Handle cases where price_b is zero to avoid division by zero
      if price_b != 0:
        expected_ratio = price_a / price_b
        self.assertEqual(getRatio(price_a, price_b), expected_ratio)
      else:
        # Assert that getRatio returns None when price_b is zero
        self.assertIsNone(getRatio(price_a, price_b))

  """ ------------ Add more unit tests ------------ """

if __name__ == '__main__':
    unittest.main()
