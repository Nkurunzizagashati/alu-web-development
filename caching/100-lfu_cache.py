#!/usr/bin/env python3

"""
    LFU caching mechanism
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU caching mechanism"""
    def __init__(self):
        """Initialize the LFUCache."""
        super().__init__()
        self.frequency = {}  # Dictionary to keep track of the frequency of each key
        self.order = []  # List to track the insertion order for LRU within LFU

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
        else:
            self.frequency[key] = 1

        self.cache_data[key] = item
        self.order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the least frequent key(s)
            min_freq = min(self.frequency.values())
            least_frequent_keys = [k for k,
                                    v in self.frequency.items()
                                     if v == min_freq]

            if len(least_frequent_keys) > 1:
                # Use LRU to choose which one to discard
                for k in self.order:
                    if k in least_frequent_keys:
                        least_recently_used_key = k
                        break
            else:
                least_recently_used_key = least_frequent_keys[0]

            # Discard the least recently used key
            del self.cache_data[least_recently_used_key]
            del self.frequency[least_recently_used_key]
            self.order.remove(least_recently_used_key)
            print(f"DISCARD: {least_recently_used_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is None:
            return None

        if key in self.cache_data:
            self.frequency[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data.get(key)
        
        return None
