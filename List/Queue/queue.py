# ADT Queue
# Queue() 创建一个空的队列，返回值为Queue对象
# enqueue(item) 将数据项item添加到队尾，无返回值
# dequeue() 从队首移除数据项，返回值为队首数据项，队列被修改
# isEmpty() 测试是否空队列，返回值为布尔值
# size() 返回队列中数据项的个数

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
