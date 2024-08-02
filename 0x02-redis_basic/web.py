#!/usr/bin/env python3

import redis
from functools import wraps
from typing import Callable
import requests

redis_client = redis.Redis()


def cache_with_expiry(expiry: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"

            # Increment the access count
            redis_client.incr(count_key)

            print(f"Count for {url}: {redis_client.get(count_key)}")

            # Check if the page is cached
            cached_page = redis_client.get(cache_key)
            if cached_page:
                print("Returning cached page")
                return cached_page.decode('utf-8')

            # If not cached, fetch the page
            print("Fetching page from URL")
            page_content = func(url)

            # Cache the result with expiration
            redis_client.setex(cache_key, expiry, page_content)

            return page_content
        return wrapper
    return decorator


@cache_with_expiry()
def get_page(url: str) -> str:
    try:
        response = requests.get(url, timeout=5)
        return response.text
    except requests.RequestException:
        print(f"Failed to fetch {url}. Returning dummy content.")
        return f"Dummy content for {url}"


def print_redis_keys():
    print("All keys in Redis:")
    for key in redis_client.keys('*'):
        try:
            value = redis_client.get(key)
            if value is not None:
                print(f"{key}: {value}")
            else:
                print(f"{key}: (Unable to retrieve value)")
        except redis.exceptions.ResponseError:
            try:
                # Try to get the type of the key
                key_type = redis_client.type(key).decode('utf-8')
                print(f"{key}: (Type: {key_type})")
            except BaseException:
                print(f"{key}: (Unable to retrieve value or type)")
