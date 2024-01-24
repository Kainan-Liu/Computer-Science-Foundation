'''
Python中的list本质上是动态数组
具备普通数组访问效率高的优点, 以O(1)时间访问元素，同时能够实现动态扩容
添加元素至末尾时时间复杂度也是O(1)
插入, 删除元素时间复杂度仍然为O(n)
Note:
1. 动态数组在内存中的实际占用内存大小为其最大容量, 没有被赋值的部分默认初始化为0
2. _size表示数组实际含有的元素个数, _size - 1指向该动态数组的最后一个元素
'''
from typing import Optional
class DynamicArray:
    def __init__(self, default_capacity: int = 10, default_extendrate=2, store_array: Optional[list[int]] = None) -> None:
        self.capacity = default_capacity
        self.default_capacity = default_capacity #默认数组最大容量为10
        self.default_extendrate = default_extendrate #默认扩容倍数
        self.store_array = store_array if store_array else [0] * default_capacity
        self._size = len(store_array) if store_array else 0

    def size(self):
        return self._size
    
    def capacity(self):
        return self.capacity
    
    def extend_capacity(self):
        old_capacity = self._size
        new_capacity = old_capacity + (self.default_extendrate - 1) * old_capacity
        self.capacity = new_capacity # update capacity
        self.store_array = self.store_array + [0] * (new_capacity - old_capacity)
    
    def append(self, value):
        if self._size <= 0 or self._size >= self.capacity:
            self.extend_capacity()
        self.store_array[self._size] = value
        self._size += 1
    
    def insert(self, index: int, value: int):
        if self._size <= 0 or self._size >= self.capacity:
            self.extend_capacity()
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bound")
        
        for i in range(self._size - 1, index - 1, -1):
            self.store_array[i + 1] = self.store_array[i]
        self.store_array[index] = value
        self._size += 1 #更新元素数量

    def delete(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bound")
        
        for i in range(index + 1, self._size):
            self.store_array[i - 1] = self.store_array[i]
        self._size -= 1

    def clear(self):
        self.store_array = [0] * self.default_capacity
    
    def access(self, index: int):
        '''
        访问动态数组中下标为index的元素
        '''
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bound")
        return self.store_array[index]
    
    def get_array(self):
        '''
        获取该动态数组中的实际元素
        '''
        return self.store_array[:self._size]

