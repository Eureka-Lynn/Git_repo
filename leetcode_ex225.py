class MyStack:

    def __init__(self):
            self.stake=[]
    def push(self, x: int) -> None:
            self.stake.append(x)

    def pop(self) -> int:
            return self.stake.pop()

    def top(self) -> int:
            return self.stake[-1]

    def empty(self) -> bool:
            return self.stake==[]


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()