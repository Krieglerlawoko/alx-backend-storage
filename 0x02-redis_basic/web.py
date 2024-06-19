#!/usr/bin/env python3
"""
A module for caching HTTP requests and tracking access.
"""

import redis
import requests
from functools import wraps
from typing import Callable

# Initialize a Redis client
redis_client = redis.Redis()


def track_get_page(fn: Callable) -> Callable:
    """
    Decorator for get_page that:
    - Checks if URL's data is cached
    - Tracks how many times get_page is called
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """
        Wrapper that:
        - Increments the access count for the URL
        - Returns cached data if available
        - Fetches and caches data if not available
        """
        # Track the number of times the URL is accessed
        redis_client.incr(f'count:{url}')
        # Check if the URL's data is cached
        cached_page = redis_client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')
        # Fetch the data and cache it
        response = fn(url)
        redis_client.setex(url, 10, response)
        return response

    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """
    Makes an HTTP GET request to a given URL and returns the response text.
    """
    response = requests.get(url)
    response.raise_for_status()
    return response.text
