class MinStack:

    def __init__(self):
        self.stk = []
        self.f = []


    def push(self, x: int) -> None:
        self.stk.append(x)
        if len(self.f) == 0 or self.f[-1] >= x: self.f.append(x)


    def pop(self) -> None:
        if self.stk[-1] <= self.f[-1]: self.f.pop()
        self.stk.pop()

    def top(self) -> int:
        return self.stk[-1]


    def getMin(self) -> int:
        return self.f[-1]

