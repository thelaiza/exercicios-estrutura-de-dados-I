# --- Médio - leetcode.com/problems/min-stack ---

class MinStack:
    def __init__(self):
        self.stack = []      # pilha principal
        self.min_stack = []  # pilha auxiliar de mínimos

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def get_min(self):
        return self.min_stack[-1]

# --- Testes ---
# Caso 1 — exemplo clássico
s = MinStack()
s.push(-2)
s.push(0)
s.push(-3)
print(s.get_min())  # -3
s.pop()
print(s.top())      # 0
print(s.get_min())  # -2

# Caso 2 — mínimo no topo
s2 = MinStack()
s2.push(5)
s2.push(3)
s2.push(7)
print(s2.get_min())  # 3
s2.pop()
print(s2.get_min())  # 3

# Caso 3 — valores iguais
s3 = MinStack()
s3.push(2)
s3.push(2)
s3.pop()
print(s3.get_min())  # 2