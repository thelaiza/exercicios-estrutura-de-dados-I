# --- Fácil - leetcode.com/problems/reverse-linked-list ---

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next  # guarda o próximo
        current.next = prev       # inverte o ponteiro
        prev = current            # avança prev
        current = next_node       # avança current

    return prev

# --- Auxiliares para teste ---
def build_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# --- Testes ---
print_list(reverse_list(build_list([1, 2, 3, 4, 5])))  # [5, 4, 3, 2, 1]
print_list(reverse_list(build_list([1, 2])))            # [2, 1]
print_list(reverse_list(build_list([1])))               # [1]
print_list(reverse_list(build_list([])))                # []