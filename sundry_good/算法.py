"""
冒泡
快排
"""

"""
给定一个整数数组nums和一个整数目标值target,请你在该数组中找出和为目标值的
两个整数，并返回他们的数组下标
"""
nums = [2, 7, 11, 15]
target = 9


def two_sum(nums, target):
    from itertools import combinations
    for pair in combinations(nums, 2):
        if sum(pair) == target:
            return pair
        return None


"""
sa
"""
