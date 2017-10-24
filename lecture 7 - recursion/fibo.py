def fiboOld(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fiboOld(n-1) + fiboOld(n-2)

def fiboSimple(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

memo={0:0, 1:1}
def fibo(n):
    if not n in memo:
        v = fibo(n-1) + fibo(n-2)
        memo[n] = v
        return v

    else:
        return memo[n]


def fib(n):
    a,b = 0, 1
    for i in range(n):
        a,b = b, a+b

    return a

from timeit import Timer

for x in range(1, 100):
    s = "fib("+ str(x) + ")"
    t1 = Timer(s, "from fibo import fib")
    time1 = t1.timeit(3)

    s = "fibo(" + str(x) + ")"
    t2 = Timer(s, "from fibo import fibo")
    time2 = t2.timeit(3)

    # s = "fiboOld(" + str(x) + ")"
    # t3 = Timer(s, "from fibo import fiboOld")
    # time3 = t3.timeit(3)

    #print("n=%2d, fib: %8.6f, fibo: %7.6f, fiboOld: %7.6f" % (x, time1, time2, time3))
    print("n=%2d, fib: %8.6f, fibo: %7.6f" % (x, time1, time2))


