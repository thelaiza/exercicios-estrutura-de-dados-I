# Valid Parentheses - https://leetcode.com/problems/valid-parentheses/description/ - Pilhas - Fácil
# Complexidade: O(n) tempo, O(n) espaço

def isValid(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        else:
            # Fechamento sem abertura correspondente no topo
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()

    return len(stack) == 0  # pilha vazia = tudo fechado


# Testes
print(isValid("()"))        # True
print(isValid("()[]{}"))    # True
print(isValid("(]"))        # False
print(isValid("([)]"))      # False
print(isValid("{[]}"))      # True
print(isValid(""))          # True  (caso especial: string vazia)
print(isValid("]"))         # False (fechamento sem abertura)