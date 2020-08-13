# Stack 的两端对应list设置
#   可以将List的任意一端(index=0 或者 -1)设置为栈顶
#   我们选用List的末端（index=-1）作为栈顶


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
