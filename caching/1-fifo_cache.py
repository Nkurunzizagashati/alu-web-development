#!/usr/bin/env python3

"""
    a class FIFOCache that inherits from
    BaseCaching and is a caching system
    and implements a First-In-First-Out
    (FIFO) caching system
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
            assign to the dictionary self.cache_data
            the item value for the key key
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # FIFO: Remove the first key in the order list
            first_key = self.order.pop(0)
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
            returns the value in self.cache_data linked to key
        """

        if key is None:
            return None
        return self.cache_data.get(key)
