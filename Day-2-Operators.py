#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
   tp=meal_cost*(tip_percent/100)
   tx=meal_cost*(tax_percent/100)
   c=int(round(meal_cost+tp+tx))
   print(c)


if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)