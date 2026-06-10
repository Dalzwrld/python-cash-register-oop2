#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount, total, items, previous_transactions):
    self.discount = discount
    self.total = total
    self.items = items
    self.previous_transactions = previous_transactions
