# Linked-List

链表是一种线性的数据结构，链表中的每个元素是一个节点对象

链表的组成单位是[节点node]对象，每个节点包含两项数据：当前节点的值和指向节点的引用

- 单向链表：指向下一节点的引用
- 双向链表：指向前驱节点和后继节点的引用
- 图：指向邻接节点的引用

![image](https://github.com/Kainan-Liu/Computer-Science-Foundation/assets/146005327/0967cc02-9137-4a20-ad08-95ba6585b060)

链表的首个节点为“头节点”，最后一个节点为“尾节点”，指向null

## Initialization

链表的初始化分为两步：

1. 初始化各个节点对象
2. 构建节点之间的引用关系

```python
class ListNode:
    def __init__(val: int):
        self.val = val
        self.next: ListNode|None = None

n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)

n0.next = n1
n1.next =n2
```

## Accessing

根据索引访问链表中的元素效率较低，时间复杂度为O(n)

访问链表中的元素需要从头节点出发，逐个向后遍历，直至到达目标索引位置节点

## 增

链表中相邻两个节点之间插入一个新的节点，只需要改变两个节点的引用即可，时间复杂度为O(1)

新插入的节点指向后继节点，前驱节点指向新插入的节点

![image](https://github.com/Kainan-Liu/Computer-Science-Foundation/assets/146005327/0580e66e-f375-42cd-bdee-153db78834f3)

## 删

链表中删除节点，只需要改变一个节点的引用即可，时间复杂度为O(1)

![image](https://github.com/Kainan-Liu/Computer-Science-Foundation/assets/146005327/debf6880-295b-4e58-a30e-279a0bed4388)

## 查

遍历链表，判断当前遍历的节点值是否符合条件，如果符合，输出该节点在链表中的索引

查找过程为线性查找，时间复杂度为O(n)

## 链表VS数组

|          | 数组                           | 链表                               |
| -------- | ------------------------------ | ---------------------------------- |
| 存储方式 | 连续内存空间                   | 分散内存空间                       |
| 容量扩展 | 长度不可变-静态数据结构        | 灵活扩展                           |
| 内存效率 | 空间效率高，但可能占用多余空间 | 额外存储结构存储指向下一节点的引用 |
| 访问元素 | O(1)                           | O(n)                               |
| 添加元素 | O(n)                           | O(1)                               |
| 删除元素 | O(n)                           | O(1)                               |

## 常见的链表类型

- 单向链表
- 双向链表
- 环形链表

![image](https://github.com/Kainan-Liu/Computer-Science-Foundation/assets/146005327/d0c5853f-ec7a-4617-a168-fed6007699c2)

