def mendel_inherit(k, m, n):
    total_children = sum([i for i in range(1, (k + m + n))])
    dominant_children = sum([i for i in range(1, k)]) + (3/4 * sum([i for i in range(1, m)])) + (k * n) + (k * m) + ((m * n) / 2)
    return dominant_children/total_children
