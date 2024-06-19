#!/usr/bin/env python3
"""
A module with tools for request caching and tracking.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis client
redis_store = redis.Redis()

def data_cacher(method: Callable) -> Callable:
    """
    Decorator that caches output of method.
    Tracks number of times URL is accessed.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function for caching output.
        Increments request count .caches result.
        """
        redis_store.incr(f'count:{url}')
        cached_result = redis_store.get(f'result:{url}')
        if cached_result:
            return cached_result.decode('utf-8')
        
        result = method(url)
        redis_store.setex(f'result:{url}', 10, result)
        return result
    return wrapper

@data_cacher
def get_page(url: str) -> str:
    """
    Fetches content of URL.caches response.
    """
    response = requests.get(url)
    response.raise_for_status()  # Ensure handling HTTP errors
    return response.text
