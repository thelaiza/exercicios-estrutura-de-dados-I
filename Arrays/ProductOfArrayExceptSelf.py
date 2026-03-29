# Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/description/ - Array - Médio
# Complexidade: O(n) tempo, O(1) espaço extra

def productExceptSelf(nums):
    n = len(nums)
    result = [1] * n

    # Passagem da esquerda: prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Passagem da direita: suffix products multiplicados no resultado
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


# Testes
print(productExceptSelf([1, 2, 3, 4]))   # [24, 12, 8, 6]
print(productExceptSelf([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print(productExceptSelf([2, 3]))         # [3, 2]
print(productExceptSelf([1]))            # [1]