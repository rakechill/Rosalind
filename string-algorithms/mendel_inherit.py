def mendel_inherit(k, m, n):
    # probability of each type of parent being picked
    # k = homo dom, m = hetero, n = homo rec
    YY = k / sum((k, m, n))
    Yy = m / sum((k, m, n))
    yy = n / sum((k, m, n))

    #then there are crossover probabilities
    # YY * Yy = 100% of probability of getting both parent (which maybe is jus multiplication of 2 probabilities?)
    # Yy * yy = 50% of probability
    #YY * yy = 100% of prev probability

    # probability of a dominant allele
    # includes hetero AND homo dom which is confusing

    return
