#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_dig = number % 10 if number >= 0 else -(-number % 10)

if (number % 10 > 5):
    print(f"Last digit of {number} is {last_dig} and is greater than 5")
elif (number % 10 < 6 and number % 10 != 0):
    print(f"Last digit of {number} is {last_dig} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {last_dig} and is 0")
