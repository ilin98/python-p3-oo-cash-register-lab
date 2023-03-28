#!/usr/bin/env python3


class CashRegister:

  items = []

  def __init__(self, discount = 0, total = 0):
    self.discount = discount
    self.total = total

  def add_item(self, title, price, quantity = 1):
    self.title = title
    self.price = price
    self.total = self.total + (price * quantity)
    CashRegister.items.append(self.title)


  def apply_discount(self):
    if self.discount != 0:
      self.total = self.total - (self.total * self.discount * 0.01)
      print(f"After the discount, the total comes to ${int(self.total)}.")
    else:
      print("There is no discount to apply.")
