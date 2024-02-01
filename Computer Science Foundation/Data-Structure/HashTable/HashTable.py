class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next: ListNode|None = None

class ArrayLinkedListHashMap:
    def __init__(self):
        self._capacity: int = 1
        self.buckets: list[ListNode|None] = [None] * self._capacity
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
        
        index = self.hash_func(key)
        bucket = self.buckets[index]
        node = ListNode(key, value)
        if bucket:
            prev = bucket
            while bucket:
                if bucket.key == key: # 如果待插入的key已经存在，则更新key相对应的value值并返回
                    bucket.value = value
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
            value = bucket.value
            bucket = bucket.next
            self._size -=  1
            return value
        prev = bucket
        bucket = bucket.next
        while bucket:
            if bucket.key == key:
                value = bucket.value
                prev.next = bucket.next
                bucket.next = None
                self._size -= 1
                return value
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
    
    def print(self):
        '''
        转化为数组并打印输出
        '''
        res = []
        for bucket in self.buckets:
            while bucket:
                res.append([bucket.key, bucket.value])
                bucket = bucket.next
        print(res)

if __name__ == "__main__":
    myDict = ArrayLinkedListHashMap()
    myDict.update(102, "小明")
    myDict.update(103, "小红")
    myDict.update(202, "小绿")
    myDict.print()
    myDict.remove(102)
    myDict.print()
    print(myDict.get(103))
    print(myDict.get(202))
