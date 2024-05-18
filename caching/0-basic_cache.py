#!/usr/bin/env python3

"""
    This module contains a class that inherits from the BaseCaching
    class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Base cache class"""

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the
            item value for the key key.
            If key or item is None, this method should not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.
            If key is None or if the key does not exist
            in self.cache_data, return None.
        """
        if key is None:
            return None
        return self.cache_data.get(key)
