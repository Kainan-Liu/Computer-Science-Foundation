# LeetCode精选

LeetCode 链表题精选

## 链表反转

采用双指针，遍历链表时修改当前遍历节点next引用指向

![image-20240129094521589](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240129094521589.png)

```python
class Solution:
    def reverseLinkedList(self, head: ListNode|None = None):
        pre = null
        cur = head
        while cur:
            temp = cur.next
            cur.next = pre
            pre, cur = cur, temp
        return pre
```



