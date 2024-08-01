#!/usr/bin/env python3
"""
Main file for testing Cache class with new methods
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
    print(f"Test case passed for: {value}")

# Test get_str and get_int
str_key = cache.store("string_test")
int_key = cache.store(42)

print(cache.get_str(str_key))
print(cache.get_int(int_key))