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

# 十进制转换为任意进制


def dividBy2(decNumber, base):
    digits = "0123456789ABCDEF"
    remStack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base  # // 代表整除

    binString = ""
    while not remStack.isEmpty():
        binString = binString + digits[remStack.pop()]
    return binString


if __name__ == "__main__":
    print(dividBy2(233, 16))
