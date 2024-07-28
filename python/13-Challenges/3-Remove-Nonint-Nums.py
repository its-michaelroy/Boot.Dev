def remove_nonints(nums):
    ints_only = []
    for item in nums:
        if type(item) == int:
            ints_only.append(item)
    return ints_only
