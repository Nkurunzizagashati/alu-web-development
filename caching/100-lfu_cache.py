#!/usr/bin/env python3

"""
    LFU caching mechanism
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
        LFU caching mechanism
    """

    def __init__(self):
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
            puts the item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            least_frequent_keys = [k for k, v
                                   in self.frequency.items() if v == min_freq]

            least_recently_used_key = min(least_frequent_keys, key=lambda
                                           k: self.frequency.get(k,
                                            float('inf')))

            del self.cache_data[least_recently_used_key]
            del self.frequency[least_recently_used_key]
            print(f"DISCARD: {least_recently_used_key}")

    def get(self, key):
        """
            gets data from the cache
        """
        if key is None:
            return None
        # If key exists, update its frequency
        if key in self.cache_data:
            self.frequency[key] += 1
        return self.cache_data.get(key)