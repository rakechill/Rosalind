# given:  positive integers n <= 40 and k <= 5
# return: total number of rabbit pairs after n months
#         such that every pair of reproduction-age (1 month)
#         rabbits produces a litter of k rabbit pairs

def how_many_pairs(n, k):
    """ An initial population of 1 pair is assumed.
        Does not take into account the n month's new pairs.
    >>> how_many_pairs(5, 3)
    >>> 19
    """
    if n == 2:
        return 1
    if n == 3:
        return k + 1
    return k * how_many_pairs(n - 2, k) + how_many_pairs(n - 1, k)
