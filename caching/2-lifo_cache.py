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
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.order.pop()
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """
            Return the value in self.cache_data linked to key.
            If key is None or if the key does not exist in
            self.cache_data, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
