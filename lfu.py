from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_dict = {}
        self.order_dict = defaultdict(OrderedDict)
        
    def get(self, key: int) -> int:
        if key not in self.cache_dict:
            return -1
        
        value, freq = self.cache_dict.get(key)
        self.order_dict[freq].pop(key)
        if not self.order_dict[freq]:
            self.order_dict.pop(freq)
        freq += 1
        self.cache_dict[key] = (value, freq)
        self.order_dict[freq][key] = ''
        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return -1
        
        if key in self.cache_dict:
            temp_value, freq = self.cache_dict.get(key)
            self.order_dict[freq].pop(key)
            if not self.order_dict[freq]:
                self.order_dict.pop(freq)
            freq += 1
            self.cache_dict[key] = (temp_value, freq)
            self.order_dict[freq][key] = ''
            self.cache_dict[key] = (value, freq)
            return
        
        if len(self.cache_dict) == self.capacity:
            min_freq = min(self.order_dict)
            del_key, _ = self.order_dict[min_freq].popitem(last=False)
            if not self.order_dict[min_freq]:
                self.order_dict.pop(min_freq)
            self.cache_dict.pop(del_key)        
        self.cache_dict[key] = (value, 0)
        self.order_dict[0][key] = ''
