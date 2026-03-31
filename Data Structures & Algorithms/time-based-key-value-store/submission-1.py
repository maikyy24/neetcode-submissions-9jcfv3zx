class TimeMap:

    def __init__(self):
      self.store = {}  # {key: [(timestamp, value), ...]}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
      if key not in self.store:
        self.store[key] = []
      self.store[key].append([timestamp , value])

    def get(self, key: str, timestamp: int) -> str:
      if key not in self.store:
        return ""
      pairs = self.store[key]
      low = 0
      high = len(pairs) - 1
      result = ""

      while low <=high:
        mid =  (low + high) // 2
        if pairs[mid][0] <= timestamp:
          result = pairs[mid][1]
          low = mid + 1
        else:
          high = mid - 1
      return result
    