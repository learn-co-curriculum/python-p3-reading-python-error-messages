#!/usr/bin/env python3

def divide(a, b):
    assert b != 0, "Division by zero is not allowed"
    return a / b

result = divide(10, 0)
print(result)
