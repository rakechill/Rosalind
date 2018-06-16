def mendel_inherit(k, m, n):
    total_children = sum([i for i in range(1, (k + m + n))])
    DDxDD, DdxDd, DDxdd, DDxDd, Ddxdd = sum([i for i in range(1, k)]), (3/4 * sum([i for i in range(1, m)])), (k * n), (k * m), (m * n) / 2
    return (DDxDD + DdxDd + DDxdd + DDxDd + Ddxdd) / total_children
