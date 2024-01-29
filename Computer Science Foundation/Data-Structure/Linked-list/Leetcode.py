# 删除链表节点
# 给定单向链表的头指针和一个要删除的节点的值x，删除链表中值为x的节点
"""
输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为5的第二个节点, 那么在调用了你的函数之后, 该链表应变为 4 -> 1 -> 9.
"""
# 分析: 需要分两种情况讨论
# 1. 当删除的节点是链表中的第一个节点时，就等同于单向队列出队, 删除链表中的第一个元素
# 2. 当删除的节点是链表中的其他节点时, 需要有一个指针指向待删除节点的前驱节点, prev.next = cur.next
from typing import Optional

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = next
    
class Solution(object):
    def deleteNode(self, val, head: Optional[ListNode] = None):
        if head.val == val:
            head = head.next

        cur = head.next
        prev = head
        while cur:
            if cur.val == val:
                prev.next = cur.next
            prev = cur
            cur = cur.next
        return head


# 倒序访问链表元素并输出
"""
输入: head = [1,2,3,4,5]
输出: [5,4,3,2,1]
"""
# 分析: 有两种解决思路
# 1. 由于栈是一种遵循先入后出逻辑的数据结构, 因此可以先将链表元素从头到尾压入栈, 之后再依次出栈即可实现倒序访问链表元素
# 2. 递归
class Solution(object):
    def reverseLinkedListval(self, head: Optional[ListNode] = None):
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]
    
class Solution(object):
    def reverseLinkedListval(self, head: Optional[ListNode] = None):
        if not head:
            return []
        num = head.val
        return self.reverseLinkedListval(head.next) + [num]
    
# 单链表逆序--头插法
class Solution(object):
    def reverseLinkedList(self, head: Optional[ListNode]=None):
        pre = None
        cur = head
        while cur:
            temp = cur.next 
            cur.next = pre
            pre, cur = cur, temp
        return pre          