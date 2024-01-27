'''
Implementation of double-ended queue using Python
双向队列兼具栈与队列的特点, 因此能够实现更高的自由度, 在队首和队尾执行元素的插入与删除操作
'''
# Python Collections Library--deque class
from collections import deque

dequeue = deque()
dequeue.append(2) #队尾入队
dequeue.appendleft(4) #队首入队
dequeue.popleft() #队首出队
dequeue.pop() #队尾出队

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.prev: ListNode|None = None
        self.next: ListNode|None = None
    

class LinkedListDeque:
    def __init__(self) -> None:
        '''
        基于双向链表实现双向队列
        '''
        self._size: int = 0
        self.first: ListNode|None = None
        self.rear: ListNode|None = None

    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def push(self, val, is_first: bool):
        if is_first:
            self.push_first(val=val)
        else:
            self.push_last(val=val)
    
    def push_last(self, val):
        '''
        向队尾插入元素, 队尾入队
        '''
        node = ListNode(val=val)
        if self.is_empty():
            self.first = node
            self.rear = node
        else:
            self.rear.next = node
            node.prev = self.rear
            self.rear = node
        self._size += 1

    def push_first(self, val):
        '''
        向队首插入元素, 队首入队
        '''
        node = ListNode(val=val)
        if self.is_empty():
            self.first = node
            self.rear = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node
        self._size += 1
    
    def pop(self, is_first):
        if is_first:
            self.pop_first()
        else:
            self.pop_last()


    def pop_first(self):
        '''
        删除队首元素, 队首出队
        '''
        if self.is_empty():
            raise IndexError("De-queue is empty")
        num = self.first.val
        fnext = self.first.next
        if fnext is not None: #先要判断fnext是否为空，不然fnext.prev发生空指针异常
            fnext.prev = None # 断开节点, 触发垃圾回收机制
            self.first.next = None 
        self.first = fnext

        self._size -= 1

        return num

    def pop_last(self):
        '''
        删除队尾元素, 队尾出队
        '''
        if self.is_empty():
            raise IndexError("De-queue is empty")
        num = self.rear.val
        fprev = self.rear.prev
        if fprev is not None: #判断fprev是否为None,避免空指针异常
            fprev.next = None
            self.rear.prev = None
        self.rear = fprev

        self._size -= 1

        return num


class ArrayDeque:
    def __init__(self, init_size: int = 10, expand_ratio = 2) -> None:
        '''
        基于环形数组实现双向队列, 在数组的头部或尾部进行元素的插入与删除
        '''
        self.array = [0] * init_size # 静态数组, 手动实现数组的动态扩容
        self._size: int = 0 # 实际存储元素的个数
        self._capacity: int = init_size
        self.expand_ratio = expand_ratio
        self.first: int = 0 # 队首元素索引

    def size(self):
        return self._size
    
    def capacity(self):
        return len(self.array)
    
    def expand_array(self):
        old_capacity = self.capacity()
        new_capacity = self.capacity() + self.capacity() * (self.expand_ratio - 1)
        self.array = self.array + [0] * (new_capacity - old_capacity)
        self._capacity = new_capacity

    def is_empty(self):
        return self._size == 0
    
    def push(self, val, is_first: bool):
        if is_first:
            self.push_first(val=val)
        else:
            self.push_last(val=val)
    
    def push_first(self, val):
        '''
        队首入队: 将元素插入数组的头部
        '''
        if self._size == self._capacity:
            self.expand_array()
        self.first = (self.first - 1 + self.capacity()) % self.capacity()
        self.array[self.first] = val
        self._size += 1

    def push_last(self, val):
        '''
        队尾入队: 将元素插入数组的尾部
        '''
        if self._size == self._capacity:
            self.expand_array()

        rear = (self.first + self._size) % self.capacity()
        self.array[rear] = val
        self._size += 1

    def pop(self, is_first):
        if is_first:
            self.pop_first()
        else:
            self.pop_last()

    def pop_first(self):
        '''
        删除队首元素, 队首出队
        '''
        if self.is_empty():
            raise IndexError("De-queue is empty")
        num = self.array[self.first]
        self.first = (self.first + 1) % self.capacity()
        self._size -= 1
        return num
    
    def pop_last(self):
        '''
        删除队尾元素, 队尾出队
        '''
        if self.is_empty():
            raise IndexError("De-queue is empty")
        last = (self.first + self._size - 1) % self.capacity()
        num = self.array[last]
        self._size -= 1
        return num

        
