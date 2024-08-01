#!/usr/bin/env python3
"""
Main file for testing Cache class with replay function
"""
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Cache = __import__('exercise').Cache
replay = __import__('exercise').replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)