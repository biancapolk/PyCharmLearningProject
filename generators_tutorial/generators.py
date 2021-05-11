def genfibon(n):
    """
    This program generates a fibonnaci sequence up to n
    """
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

    for num in genfibon(10):
        print(num)