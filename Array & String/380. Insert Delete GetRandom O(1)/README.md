# Intuition
set 형식을 이용해서 값을 빠르게 찾도록 구현한다.
# Approach
self 형식의 set을 생성한 다음, 다른 메소드에서 불러와 사용할 수 있도록 한다.

# Complexity
- Time complexity: $$O(n)$$

- Space complexity: $$O(n)$$

# Code
```python3 []
class RandomizedSet:

    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        if val not in self.s:
            self.s.add(val)
            return True
        else: return False

    def remove(self, val: int) -> bool:
        if val in self.s:
            self.s.remove(val)
            return True
        else: return False

    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
```
