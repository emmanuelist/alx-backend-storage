#!/usr/bin/env python3
"""
Main file for testing get_page function
"""
import time
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from web import get_page

# Test with a slow website
url = "https://httpbin.org/delay/3"  # This will delay the response by 3 seconds

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