#!/usr/bin/env python3

"""
    This module contains a class LIFOCache
    that inherits from BaseCaching and implements
    LIFO caching system
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
        class LIFOCache that inherits BaseCaching
        class and implements hte LIFO caching system
    """

    def __init__(self):
        """
            an init method to inherit all the methods
            from the class this LIFOCache class is inheriting
            from
        """
        super().__init__()

    def put(self, key, item):
        """
            put method to put item into the cache.
            It assigns to the dictionary self.cache_data
            the item value for the key key
        """