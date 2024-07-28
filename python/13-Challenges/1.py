# 1 to n summation
def number_sum(n):
    total = 0

    for num in range(1, n + 1):
        total += num
    return total
