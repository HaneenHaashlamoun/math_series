def fibonacci(n):
    #Base Case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    #Base Case
    if n <= 1:
        if n == 0:
            return 2
        else:
            return 1
    return lucas(n-1) + lucas(n-2)


def sum_series(n, first=0, second=1):
    if n == 0:
        #Base Case
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)
print(sum_series(3, 1, 2))
print(fibonacci(5))
print(lucas(5))