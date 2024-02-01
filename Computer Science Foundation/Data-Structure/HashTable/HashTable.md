# HashTable

哈希表[散列表]，是一种基于数组和链表实现的数据结构，它通过建立**key-value之间的映射**，实现元素的**高效查询**。能够在O(1)时间内获取相对应的值

| 操作         | 数组 | 链表 | 哈希表 |
| ------------ | ---- | ---- | ------ |
| 尾部添加元素 | O(1) | O(1) | O(1)   |
| 查询元素     | O(n) | O(n) | O(1)   |
| 删除元素     | O(n) | O(n) | O(1)   |

**哈希表进行增删改查的时间复杂度都是O(1)**

将哈希表底层的数组中的每个空位称为**桶bucket**, bucket中存储的是key-value pair

哈希函数将key的值域空间映射到数组索引的值域空间(较大的输入空间映射到较小的输入空间)，我们可以**通过哈希函数得到key值对应的键值对在数组中的存储位置**，从而实现元素的高效查询

![image-20240201103608935](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240201103608935.png)

## Python哈希表及常用操作

Python中的字典本质上是哈希表，常见操作包括: 初始化，查询键值对，添加键值对，删除键值对

```python
# initialization
hmap = {}

# 添加键值对
hmap[10222] = "小哈"
hmap.update({10343: "小哈"})

# 删除键值对
hmap.pop(10222)

# 查询键值对
name: str = hmap[10343]
```

遍历哈希表的三种方式：遍历键值对，遍历键，遍历值

```python
for key, value in hmap.items():
    print(key, "->", value)
for key in hmap.keys():
    print(key)
for value in hmap.values():
    print(value)
```

## Implementation

基于数组和链表实现的哈希表， 将键值对作为链表节点，将所有发生冲突的键值对都存储在同一链表中

![image-20240201122048025](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240201122048025.png)

基于链式地址实现的哈希表虽能有效的处理哈希冲突，但存在以下局限性:

- 占用空间增大：链表包含节点指针
- 查询效率较低：对于发生哈希冲突的键值对，需要线性遍历链表来查找对应元素

```python
class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: ListNode|None = None

class ArrayLinkedListHashMap:
    def __init__(self):
        self._capacity: int = 100
        self.buckets: List[ListNode|None] = [None] * self._capacity
        self._size: int = 0
        self.load_threshold = 2.0 / 3.0 #负载因子阈值
        self.extend_rate = 2
    
    def load_factor(self):
        '''
        负载因子：获取数组中存储的键值对的个数占总容量的比率
        '''
        return self._size / self._capacity
    
    def capacity(self):
        return self._capacity
   	
    def extend_capacity(self):
        buckets = self.buckets # 暂存原哈希表
        old_capacity = self.capacity()
        new_capacity = old_capacity + (self.extend_rate - 1) * old_capacity
        self.buckets = [None] * new_capacity
        self._capacity = new_capacity
        # 将键值对搬运到新的buckets
        for bucket in buckets:
            while bucket:
                key = bucket.key
                value = bucket.value
                self.update(key, value)
                bucket = bucket.next
    
    def hash_func(self, key):
        index = key % self._capacity
        return index
    
    def update(self, key, value):
        if self.load_factor() > self.load_threshold:
            self.extend_capacity()
        
        index = hash_func(key)
        bucket = self.buckets[index]
        node = ListNode(key, value)
        if bucket:
            prev = bucket
            while bucket:
                if bucket.key == key: # 如果待插入的key已经存在，则更新key相对应的value值并返回
                    bucket.value =  value
                    return
                prev = bucket
                bucket = bucket.next
            prev.next = node
        else:
             self.buckets[index] = node
        self._size += 1
    
    def remove(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        if bucket is None:
            raise IndexError("keyError: key is not found in dict")
        if bucket.key == key:
            bucket = bucket.next
            self._size -=  1
            return
        prev = bucket
        bucket = bucket.next
        while bucket:
            if bucket.key == key:
                prev.next = bucket.next
                bucket.next = None
                self._size -= 1
                return
            prev, bucket = bucket, bucket.next
        raise IndexError("keyError: Key is not found in dict")
        
    def get(self, key):
        index = self.hash_func(key)
        bucket = self.buckets[index]
        while bucket:
            if bucket.key == key:
                return bucket.value
            bucket = bucket.next
        raise IndexError("keyError: key is not found in dict")
```

特别注意的是：当我们扩容哈希表时，需要将原始哈希表中的所有键值对移动到新的哈希表中，但原键值对存放的位置发生改变, `hash_func = hash(key) % self.capacity`, `self.capacity`发生改变

当链表很长时，查询效率O(n)，此时可以**将链表转化为”红黑树“，从而将查询操作的时间复杂度优化至O(logn)**

-------

## 哈希冲突

哈希函数的作用是将**所有key构成的输入空间映射到数组所有索引构成的输出空间**，而输入空间往往大于输出空间，因此存在”多个输入对应一个输出“的情况 -> 哈希冲突hash collision

哈希冲突：有多种解决方案

- 扩容哈希表来减少冲突

  哈希表容量越大，发生哈希冲突的可能性越低

  缺点是性能下降，将所有键值对从原哈希表迁移至新哈希表非常耗时，并且**由于哈希表容量capacity改变，需要通过哈希函数重新计算所有键值对的存储位置**，进一步增加了计算开销

- 链式地址

  链式地址存在一些局限性：

  - 占用空间增大
  - 查询效率降低：需要线性遍历链表来查找对应元素

- 

