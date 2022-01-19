class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def empty(self):
        if len(self.items) == 0:
            return 'YES'
        else:
            return 'NO'
    def query(self):
        return self.items[-1]

m = int(input())
S = Stack()
for i in range(m):
    inp = input().split()
    if inp[0] == 'push':
        S.push(int(inp[1]))
    if inp[0] == 'pop':
        S.pop()
    if inp[0] == 'empty':
        print(S.empty())
    if inp[0] == 'query':
        print(S.query())
