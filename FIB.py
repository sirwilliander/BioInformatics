# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)


def fib(n, k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1, k) + k*fib(n - 2, k)


n = 28
k = 4

print(fib(n, k))
