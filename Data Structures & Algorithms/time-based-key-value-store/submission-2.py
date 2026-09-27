class TimeMap:

    def __init__(self):
        self.s = {}
        self.t = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key] = [] if key not in self.s else self.s[key]
        self.t[key] = [] if key not in self.t else self.t[key]
        self.s[key].append(value)
        self.t[key].append(timestamp)
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.t:
            return ""
        ts = self.t[key]
        i = 0
        j = len(ts) - 1
        print(self.s, self.t, ts)
        while i <= j:
            mid = i + (j-i)//2
            if ts[mid] > timestamp:
                j = mid - 1
            elif ts[mid] < timestamp:
                i = mid + 1
            else:
                return self.s[key][mid]
        return self.s[key][j] if j >= 0 else ""
