#!/bin/usr/bash python3
import redis
import uuid
from typing import Union, Callable

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
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes, int, float]:
        """
        Retrieves the data associated with the given key from the cache and applies an optional transformation function.

        Parameters
        ----------
        key : str
            The key of the data to be retrieved from the cache.
        fn : Callable, optional
            An optional transformation function to be applied to the retrieved data (default is None).

        Returns
        -------
        Union[str, bytes, int, float]
            The retrieved data, possibly transformed by the given function.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        Retrieves the data associated with the given key from the cache and returns it as a string.

        Parameters
        ----------
        key : str
            The key of the data to be retrieved from the cache.

        Returns
        -------
        str
            The retrieved data as a string.
        """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """
        Retrieves the data associated with the given key from the cache and returns it as an integer.

        Parameters
        ----------
        key : str
            The key of the data to be retrieved from the cache.

        Returns
        -------
        int
            The retrieved data as an integer.
        """
        return self.get(key, fn=int)