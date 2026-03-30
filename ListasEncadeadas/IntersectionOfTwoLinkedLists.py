class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    while pA != pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA

    return pA

    # Testes
    def build_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")