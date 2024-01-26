'''
implementation of Queue using Array and LinkedList
'''
class ListNode:
    def __init__(self, val = 0) -> None:
        self.val = val
        self.next: ListNode|None = ListNode
    
class LinkedListQueue:
    def __init__(self) -> None:
        self.first: ListNode|None = None
        self.rear: ListNode|None = None
        self._size: int = 0
    
    def is_empty(self):
        '''
        Queue is empty or not
        '''
        return not self.first
    
    def size(self):
        return self._size
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.first.val
    
    def push(self, val):
        node = ListNode(val=val)
        if self.is_empty():
            self.first = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        num = self.peek()
        self.first = self.first.next
        self._size -= 1
        return num

class ArrayQueue:
    def __init__(self) -> None:
        '''
        数组为环形数组, 使得队列能够重复利用删除元素后的无效空间, 同时需要能够实现动态扩容
        first_index: 队列第一个元素的索引
        rear_index: size + first_index
        '''
        self.array = [0] * 10 # initial capacity
        self.first_index: int = 0
        self._capacity: int = 10
        self._size: int = 0 # 数组中实际含有的元素个数
        self.expand_ratio = 2 #数组扩容的倍数

    @property
    def size(self):
        return self._size
    
    def is_empty(self):
        return self.size == 0
    
    @property
    def capacity(self):
        return self._capacity
    
    def expand_array(self):
        new_capacity = self.capacity + self.capacity * (self.expand_ratio - 1)
        self.array = self.array + [0] * new_capacity
        self.capacity = new_capacity

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.array[self.first_index]

    def push(self, val):
        '''
        入队: 插入至数组末尾
        '''
        if self.size == self.capacity:
            self.expand_array()
        rear = (self.first_index + self.size) % self.capacity # 队列最后一个元素的下一个位置的索引
        self.array[rear] = val
        self._size += 1
    
    def pop(self):
        '''
        出队: 删除数组第一个元素[first + 1, rear)
        '''
        val = self.peek()
        self.first_index = (self.first_index + 1) % self.capacity
        self._size -= 1
        return val 


