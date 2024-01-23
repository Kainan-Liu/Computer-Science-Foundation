'''
Initialization and CRUD for Linked-List
'''
class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: ListNode|None = None

# Initialization
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)

n0.next = n1
n1.next = n2

# access
def access(n0: ListNode, index: int):
    head = n0
    for _ in range(index):
        if not head:
            return None
        head = head.next
    return head

# 增
def add(n0: ListNode, p: ListNode):
    '''
    step1: 新节点指向右节点
    step2: 左节点指向新节点
    '''
    right = n0.next
    p.next = right
    n0.next = p

# 删
def delete(n0: ListNode):
    '''
    示例: 删除链表头节点的后一个节点
    '''
    delete_node = n0.next
    next_node = delete_node.next
    n0.next = next_node

# 查
def search(n0: ListNode, val: int):
    '''
    查找链表中是否存在值为val的节点, 如果存在, 输出该节点的索引
    '''
    head = n0 # head表示遍历链表的当前位置
    index = 0
    while not head:
        if head.val == val:
            return index
        index += 1
        head = head.next
    return -1
