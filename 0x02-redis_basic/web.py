#!/usr/bin/env python3

import redis
from functools import wraps
from typing import Callable
import requests

# Initialize Redis client
redis_client = redis.Redis()


def cache_with_expiry(expiry: int = 10) -> Callable:
    """
    Decorator factory that creates a caching decorator
    with a specified expiry time.

    Args:
    expiry (int): The expiration time for cached items
    in seconds. Default is 10 seconds.

    Returns:
    Callable: A decorator function.
    """

    def decorator(func: Callable) -> Callable:
        """
        Decorator that adds caching functionality to the decorated function.

        Args:
        func (Callable): The function to be decorated.

        Returns:
        Callable: The wrapper function.
        """

        @wraps(func)
        def wrapper(url: str) -> str:
            """
            Wrapper function that implements caching logic.

            Args:
            url (str): The URL to fetch or retrieve from cache.

            Returns:
            str: The page content, either from cache or freshly fetched.
            """
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"

            # Increment the access count for the URL
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
    """
    Fetches a web page from the given URL.

    This function is decorated with @cache_with_expiry(),
    so it implements caching.

    Args:
    url (str): The URL to fetch.

    Returns:
    str: The content of the web page or a dummy content if the fetch fails.
    """
    try:
        response = requests.get(url, timeout=5)
        return response.text
    except requests.RequestException:
        print(f"Failed to fetch {url}. Returning dummy content.")
        return f"Dummy content for {url}"


def print_redis_keys():
    """
    Prints all keys and their values (if possible) stored in Redis.

    This function attempts to print the value of each key.
    If it can't retrieve the value,
    it tries to print the type of the key. If both fail,
    it prints an error message.
    """
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
