# Link: leetcode.com/problems/middle-of-the-linked-list
# Nivel Fácil - Complexidade de tempo: O(n); Complexidade de espaço: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Função auxiliar para testes
def build_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


# Testes
head = build_list([1,2,3,4,5])
print(middleNode(head).val)  # 3

head = build_list([1,2,3,4,5,6])
print(middleNode(head).val)  # 4