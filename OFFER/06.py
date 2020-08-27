class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        stack = []
        while head:
            stack.push(head.val)
            head = head.next
        while stack:
            res.append(stack.pop())
        return res
