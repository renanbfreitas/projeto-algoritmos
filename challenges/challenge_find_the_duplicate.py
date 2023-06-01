def find_duplicate(nums):
    for num in nums:
        if type(num) != int or num < 0:
            return False
        if nums.count(num) > 1:
            return num
    return False


# Teste do Requisito
# print(find_duplicate([1, 3, 4, 2, 2]))
