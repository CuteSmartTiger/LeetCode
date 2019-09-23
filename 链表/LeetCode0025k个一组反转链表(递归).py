# 递归方法
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 记录
        cur = head
        count = 0
        while count != k and cur:
            cur = cur.next
            count += 1
        if count == k:
            # res 为反转后链表的首节点
            res = self.reverseKGroup(cur, k)
            # 反转
            while count:
                # 存储当前反转段落的首节点的下一节点
                temp = head.next
                # 将首节点next指向返回的res
                head.next = res

                res = head
                head = temp
                count -= 1

            # res 为反转之后的首节点 将其赋值给head以便return返回
            head = res

        return head