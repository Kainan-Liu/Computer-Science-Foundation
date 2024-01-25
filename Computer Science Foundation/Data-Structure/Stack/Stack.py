'''
Python中没有内置的Stack, 我们可以直接使用动态数组实现栈的功能, 忽略与栈无关的操作
'''
# 基于链表实现栈
import copy

class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val = val
        self.next: ListNode|None = None

class LinkedListStack:
    def __init__(self) -> None:
        self.head: ListNode|None = None
        self._size: int = 0
    
    def push(self, val: int):
        '''
        入栈: 将元素添加至栈顶
        '''
        # 对于基于链表实现的栈，使用"头插法"将待插入的元素插入链表的头节点
        node = ListNode(val=val)
        node.next = self.head
        self.head = node
        self._size += 1

    def pop(self):
        '''
        出栈: 删除栈顶元素-删除链表的头节点
        同时返回出栈元素的值
        '''
        num = self.peek()
        self.head = self.head.next
        self._size -= 1
        return num
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return not self.head
        
    def peek(self):
        '''
        访问栈顶元素
        '''
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.head.val
    
    def to_list(self):
        if not self.head:
            return []
        arr = []
        node = copy.deepcopy(self.head)
        while node:
            arr.append(node.val)
            node = node.next

        return arr[::-1]

# 基于动态数组实现栈
class ArrayStack:
    def __init__(self) -> None:
        self.stack = []
        self._size: int = len(self.stack)
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.stack == []
    
    def peek(self):
        '''
        访问栈顶元素
        '''
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.stack[-1]
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        val = self.peek()
        self.stack.pop()
        return val
    
    def to_list(self):
        return self.stack
