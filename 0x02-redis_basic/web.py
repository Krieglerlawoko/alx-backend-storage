#!/usr/bin/env python3
"""
Web Cache Module
"""

import redis
import requests
from typing import Callable

redis_client = redis.Redis()


def get_page(url: str) -> str:
    """Fetch the HTML content of
    a URL and cache it in Redis"""
    key = f"count:{url}"
    redis_client.incr(key)
    cached_page = redis_client.get(url)
    if cached_page:
        return cached_page.decode('utf-8')

    response = requests.get(url)
    html_content = response.text
    redis_client.setex(url, 10, html_content)
    return html_content
