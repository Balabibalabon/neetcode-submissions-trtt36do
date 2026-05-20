class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(f"stack 存入 {val}")
        self.mininumber = min(self.mini[-1], val) if self.mini else val
        self.mini.append(self.mininumber)
        print(f"mini stack 存入 {self.mininumber}")

    def pop(self) -> None:
        print(f"stack 移除 {self.stack[-1]}")
        del self.stack[-1]
        print(f"mini stack 移除 {self.mini[-1]}")
        del self.mini[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mini[-1]
        
