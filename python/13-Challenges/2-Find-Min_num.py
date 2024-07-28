def find_min(nums):
    min_value = float("inf")

    for num in nums:
        if num < min_value:
            min_value = num

    return min_value
