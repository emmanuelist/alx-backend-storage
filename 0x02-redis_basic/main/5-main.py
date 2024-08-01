#!/usr/bin/env python3
"""
Main file for testing get_page function
"""
import time
from web import get_page

# Test with a slow website
url = "http://slowwly.robertomurray.co.uk/delay/1000/url/https://www.example.com"

# First call (should be slow)
start_time = time.time()
content = get_page(url)
print(f"First call took {time.time() - start_time:.2f} seconds")

# Second call (should be fast, cached)
start_time = time.time()
content = get_page(url)
print(f"Second call took {time.time() - start_time:.2f} seconds")

# Wait for cache to expire (11 seconds)
print("Waiting for cache to expire...")
time.sleep(11)

# Third call (should be slow again)
start_time = time.time()
content = get_page(url)
print(f"Third call took {time.time() - start_time:.2f} seconds")

# Check count
import redis
r = redis.Redis()
print(f"Page was accessed {r.get(f'count:{url}').decode('utf-8')} times")