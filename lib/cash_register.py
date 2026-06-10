#!/usr/bin/env python3
cash = float(input("Enter the amount you wanna deposit: "))
class CashRegister:
  cash = 0
  
  def __init__(self, discount, total, items, previous_transactions):
    self.discount = discount
    self.total = total
    self.items = items
    self.previous_transactions = previous_transactions

  
