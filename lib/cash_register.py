#!/usr/bin/env python3
item = input("Enter the item you wanna buy: ")
quantity = int(input("Enter the number of items: "))
price = float(input("Enter the price of the item: "))
class CashRegister:
  total_amount = 0
  total_discount = 0
  total_items = []
  previous_transactions = []

  def __init__(self, discount, total, items, previous_transactions):
    self.discount = discount
    self.total = total
    self.items = items
    self.previous_transactions = previous_transactions

  @property
  def discount(self):
    return self._discount
  
  @discount.setter
  def discount(self, value):
    if isinstance(value, int) and 0 <= value <= 100:
      self._discount = value
    else:
      raise ValueError("Not valid discount.")
    
  def add_item(self, item, price, quantity=1):
    self.total += price * quantity

    for _ in range(quantity):
      self.items.append(item)

    self.previous_transactions.append({
      "item": item,
      "price": price,
      "quantity": quantity
    })
