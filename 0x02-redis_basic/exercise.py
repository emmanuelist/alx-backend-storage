#!/usr/bin/env python3

import functools
import uuid
from typing import Callable, Union

import redis


def replay(method: Callable):
    """
    Replays the call history of a method by
    printing the input and output values.

    Args:
        method (Callable): The method to replay.
    """
    redis_client = redis.Redis()
    method_name = method.__qualname__
    inputs = redis_client.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method_name}(*{input_data.decode('utf-8')}) -> "
              f"{output_data.decode('utf-8')}")


def count_calls(method: Callable) -> Callable:
    """
    A decorator to count the number of calls to a method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    A decorator to store the call history of a method.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The decorated method.
    """
    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


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
        Initializes the Cache instance by creating a Redis
        client and flushing the database.

    store(data: Union[str, bytes, int, float]) -> str
        Stores the given data in the cache and returns a
        unique key for the stored data.
    """

    def __init__(self):
        """
        Initializes the Cache instance by creating a
        Redis client and flushing the database.

        Note
        ----
        This will delete all existing data in the Redis database.
        Use with caution.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the given data in the cache and returns
        a unique key for the stored data.

        Parameters
        ----------
        data : Union[str, bytes, int, float]
            The data to be stored in the cache.
            It can be of type str, bytes, int, or float.

        Returns
        -------
        str
            A unique key for the stored data.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """
        Retrieves the data associated with the given key from the cache
        and applies an optional transformation function.

        Parameters
        ----------
        key : str
            The key of the data to be retrieved from the cache.
        fn : Callable, optional
            An optional transformation function to be applied to
            the retrieved data (default is None).

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
        Retrieves the data associated with the given key
        from the cache and returns it as a string.

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
        Retrieves the data associated with the given key from
        the cache and returns it as an integer.

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