# Add Two Numbers - https://leetcode.com/problems/add-two-numbers/description/ - Listas Encadeadas - Médio
# Complexidade: O(max(m, n)) tempo, O(max(m, n)) espaço

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)  # nó sentinela para simplificar a lógica
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)

        current = current.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next  # pula o sentinela


# Helpers para teste
def list_to_nodes(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Testes
# 342 + 465 = 807  →  [2,4,3] + [5,6,4] = [7,0,8]
l1 = list_to_nodes([2, 4, 3])
l2 = list_to_nodes([5, 6, 4])
print(nodes_to_list(addTwoNumbers(l1, l2)))  # [7, 0, 8]

# 0 + 0 = 0
l1 = list_to_nodes([0])
l2 = list_to_nodes([0])
print(nodes_to_list(addTwoNumbers(l1, l2)))  # [0]

# 999 + 1 = 1000  →  carry se propaga até criar novo nó
l1 = list_to_nodes([9, 9, 9])
l2 = list_to_nodes([1])
print(nodes_to_list(addTwoNumbers(l1, l2)))  # [0, 0, 0, 1]