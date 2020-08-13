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


# 栈的第一个应用，简单括号匹配：’（（（）））‘
def perChecker(symbolString):
    s = Stack()
    index = 0
    balance = True

    while index < len(symbolString) and balance:
        symbol = symbolString[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            s.pop()
        index = index+1

    if balance and s.isEmpty():
        return True
    else:
        return False


if __name__ == "__main__":
    symbolString = "(()())"
    print(perChecker(symbolString))
