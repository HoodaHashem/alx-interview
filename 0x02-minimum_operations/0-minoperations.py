def minOperations(n):
    count = 0
    x = 1
    if n == 1:
        return 1
    if n == 0:
        return count
    x *= 2
    past = x
    count += 2
    while x < n:
        if n % x == 0:
            x *= 2
            past = x
            count += 2
        if n % x != 0:
            x += past
            count += 1
    return count
