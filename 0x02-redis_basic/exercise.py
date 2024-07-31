#!/bin/usr/bash python3
import redis
import uuid
from typing import Union

class Cache:
    """
    A class used to manage data in a Redis cache.

    Attributes
    ----------
    _redis : redis.Redis
        A Redis client instance used to interact with the cache.

    Methods
    -------
    __init__()
        Initializes the Cache instance by creating a Redis client and flushing the database.

    store(data: Union[str, bytes, int, float]) -> str
        Stores the given data in the cache and returns a unique key for the stored data.

    Examples
    --------
    >>> cache = Cache()
    >>> key = cache.store("Hello, World!")
    >>> print(key)
    'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
    """

    def __init__(self):
        """
        Initializes the Cache instance by creating a Redis client and flushing the database.

        Note
        ----
        This will delete all existing data in the Redis database. Use with caution.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in the cache and returns a unique key for the stored data.

        Parameters
        ----------
        data : Union[str, bytes, int, float]
            The data to be stored in the cache. It can be of type str, bytes, int, or float.

        Returns
        -------
        str
            A unique key for the stored data.

        Examples
        --------
        >>> cache = Cache()
        >>> key1 = cache.store("Hello, World!")
        >>> key2 = cache.store(12345)
        >>> key3 = cache.store(b"Hello, World!")
        >>> print(key1, key2, key3)
        'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key