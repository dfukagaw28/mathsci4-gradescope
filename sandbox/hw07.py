def souwa(n):
    if n < 1:
        return 0
    return souwa(n-1) + n
