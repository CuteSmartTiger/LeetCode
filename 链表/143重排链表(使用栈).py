# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        stack = []
        p = head
        while p:
            stack.append(p)
            p = p.next
        n = len(stack)
        count = (n-1)//2 # 需要从栈中弹出的元素数量
        cur = head
        while count:
            temp = stack.pop()
            temp.next = cur.next
            cur.next = temp
            cur = temp.next
            count -=1
        stack.pop().next = None  # 这一步很重要
        return head
