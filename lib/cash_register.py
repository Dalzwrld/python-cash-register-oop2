#!/usr/bin/env python3
cash = float(input("Enter the amount you wanna deposit: "))
class CashRegister:
  cash = 0
  total_amount = 0
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