class TimeMap:

    def __init__(self):
        self.hash_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = {}
        if timestamp not in self.hash_map[key]:
            self.hash_map[key][timestamp] = []
        self.hash_map[key][timestamp].append(value)
        return None
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        seen = 0
        for time in self.hash_map[key]:
            if time <= timestamp:
                seen = max(seen, time)
        
        return "" if seen == 0 else self.hash_map[key][seen][-1]

        
