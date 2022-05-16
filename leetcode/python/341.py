class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def dfs(l):
            if l.isInteger(): self.q.append(l.getInteger())
            else:
                for v in l.getList(): dfs(v)
        self.q = []
        self.k = 0
        for l in nestedList: dfs(l)

    def next(self) -> int:
        res = self.q[self.k]
        self.k += 1
        return res

    def hasNext(self) -> bool:
        return self.k < len(self.q)
