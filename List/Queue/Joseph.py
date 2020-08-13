

# 约瑟夫问题：将一群人围成一圈，然后将一个土豆在这一圈人中进行传递，规定一个数字，到疏导规定的数字后，拿到土豆的那个人出圈
# 一直到这个圈里只有一个人
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
# 问题的解决，使用队列。
# 首先：将这群人加入到队列中，然后规定队首的人持有土豆，通过队首的人出队列然后在加到队尾来模拟土豆的传递


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
    return simqueue.dequeue()


if __name__ == "__main__":
    print(hotPotato(["Bill", "David", "Suan", "Jane", "Kent", "Brad"], 7))
