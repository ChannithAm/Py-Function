#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File              : accountant.py
# Author            : Channith Am <amcnith@gmail.com>
# Date              : 29.09.2017
# Last Modified Date: 29.09.2017
# Last Modified By  : Channith Am <amcnith@gmail.com>

class Accountant():
    """Manage a bank account."""
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

