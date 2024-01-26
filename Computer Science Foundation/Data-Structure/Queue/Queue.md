# Queue

队列[Queue]是一种遵循**先入先出**逻辑的线性数据结构，可以由数组/链表实现

- 队首：位于队列头部的元素
- 队尾：位于队列尾部的元素

将元素插入队尾的操作称为“入队”(push)，删除队首元素称为“出队”(pop)

![image-20240126174134024](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240126174134024.png)

Python中Collections库提供了deque类，我们可以将其视为队列使用

```python
from collections import deque

queue = deque()

# 入队
queue.append(1)
queue.append(3)

# 出队
queue.popleft()
```

队列的基本操作&时间复杂度

| operation | description  | 时间复杂度 |
| --------- | ------------ | ---------- |
| push()    | 入队         | O(1)       |
| pop()     | 出队         | O(1)       |
| peek()    | 访问队首元素 | O(1)       |

----------

## Implementation

### LinkedList-Queue

基于链表实现的队列，将链表的“头节点”视为队首，将“尾节点”视为队尾

入队：将待添加的元素插入至链表尾节点之后

出队：删除头节点

### ArrayQueue

基于数组实现的队列

入队：将元素添加至数组的末尾-append

出队：删除数组的第一个元素

对于数组而言，在进行删除操作时，时间复杂度O(n); 为了防止出队操作效率较低，我们可以定义一个变量`front`指向队首元素的索引，`front + size`就指向了数组中的最后一个元素的下一个位置`rear`

![image-20240126182417980](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240126182417980.png)

- front: 指向队首元素
- rear：指向队尾元素的下一个位置

在不断执行入队和出队的过程中，`front`和`rear`指针一直在向右移动，为了能够将删除元素后的无效空间重新利用，我们将**使用环形数组实现队列**, 使得`front`和`rear`能够回到数组头部继续遍历
