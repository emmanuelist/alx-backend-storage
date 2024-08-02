import sys
import os
import time

# Add the parent directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from web import get_page, print_redis_keys, redis_client

# Use the correct URL
url = "http://slowwly.robertomurray.co.uk"

# First call
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

# Print all Redis keys
print_redis_keys()

# Check count
count = redis_client.get(f'count:{url}')
if count:
    print(f"Page was accessed {count.decode('utf-8')} times")
else:
    print(f"No count found for URL: {url}")
    