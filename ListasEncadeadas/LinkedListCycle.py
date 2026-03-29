# Linked List Cycle - https://leetcode.com/problems/linked-list-cycle/description/ - Listas Encadeadas - Fácil
# Complexidade: O(n) tempo, O(1) espaço

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False


# Helper para criar lista com ciclo nos testes
def make_list(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]  # cria o ciclo
    return nodes[0] if nodes else None

# Testes
print(hasCycle(make_list([3, 2, 0, -4], 1)))  # True  (ciclo em pos 1)
print(hasCycle(make_list([1, 2], 0)))          # True  (ciclo em pos 0)
print(hasCycle(make_list([1], -1)))            # False (sem ciclo)
print(hasCycle(None))                          # False (lista vazia)