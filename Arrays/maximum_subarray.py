# --- Médio - leetcode.com/problems/maximum-subarray ---

def max_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]

    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum

# --- Testes ---

# Caso 1 — exemplo clássico
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

# Caso 2 — todos positivos
print(max_subarray([1, 2, 3, 4]))                       # 10

# Caso 3 — todos negativos (retorna o menos negativo)
print(max_subarray([-3, -1, -2]))                       # -1

# Caso 4 — um só elemento
print(max_subarray([5]))                                 # 5