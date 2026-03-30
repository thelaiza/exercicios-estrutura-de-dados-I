# Link: leetcode.com/problems/implement-queue-using-stacks
# Nivel Médio - Complexidade de tempo: O(1) amortizado; Complexidade de espaço: O(n)

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x):
        self.in_stack.append(x)

    def pop(self):
        self.peek()
        return self.out_stack.pop()

    def peek(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]

    def empty(self):
        return not self.in_stack and not self.out_stack


# Testes
q = MyQueue()
q.push(1)
q.push(2)
print(q.peek())  # 1
print(q.pop())   # 1
print(q.empty()) # False