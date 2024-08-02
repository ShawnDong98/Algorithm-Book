"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead,分别完成在队列尾部插入节点和在队列头部删除节点的功能。
"""

class CQueue:
    def __init__(self):
        super().__init__()
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, x):
        self.stack1.append(x)

    def deleteHead(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            
        if not self.stack2:
            return -1
        
        return self.stack2.pop()