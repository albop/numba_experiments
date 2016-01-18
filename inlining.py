from numba import njit

@njit
def jitted_fun(x):
    return x**2

@njit
def f1_manual(N):
    t = 0.0
    x = 2.0
    for i in range(N):
        t = (x)**2
    return t

@njit
def f1_auto(N):
    t = 0.0
    x = 2.0
    for i in range(N):
        t = jitted_fun(x)
    return t

@njit
def f2_manual(x,N):
    t = 0.0
    for i in range(N):
        t = (x)**2
    return t

@njit
def f2_auto(x,N):
    t = 0.0
    for i in range(N):
        t = jitted_fun(x)
    return t


x = 2.0
N = 100000000

f1_manual(N)
f1_auto(N)
f2_manual(x,N)
f2_auto(x,N)

import time
t1 = time.time()
f1_manual(N)
t2 = time.time()
f1_auto(N)
t3 = time.time()
f2_manual(x,N)
t4 = time.time()
f2_auto(x,N)
t5 = time.time()
print(t2-t1)
print(t3-t2)
print(t4-t3)
print(t5-t4)
