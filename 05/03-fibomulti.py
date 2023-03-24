import multiprocessing

def fib(n):
    """computing the Fibonacci in an inefficient way
    was chosen to slow down the CPU."""
    if n <= 2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

p = multiprocessing.Pool()
print(p.map(fib,[40,39,38,37,36,35]))
