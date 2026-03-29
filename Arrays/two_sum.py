# --- Fácil - leetcode.com/problems/two-sum ---

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

# --- Testes ---
print(two_sum([2, 7, 11, 15], 9))   # esperado: [0, 1]
print(two_sum([3, 3], 6))            # esperado: [0, 1]
print(two_sum([1, 4, 6, 8], 14))     # esperado: [2, 3]
print(two_sum([-3, 4, 3, 90], 0))    # esperado: [0, 2]