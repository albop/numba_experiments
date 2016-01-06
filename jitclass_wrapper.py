# Given a function $f$, a strictly positive integer and a real number $x$ we want to define the function $I(f)$ such that: $I(f)(x)=\frac{1}{N} \sum_{n=0}^{N-1} f(\frac{n}{N-1} x) $

# ## code

def fjit(fun):
    'just-in-time compile a function by wrapping it in a singleton class'
    
    from numba import jitclass
    import time
    
    # the function is jitted first
    jitted_fun = njit(fun)

    # Generate a random class name like 'Singleton_Sat_Jan__2_18_08_32_2016'
    classname = 'Singleton_' + time.asctime().replace(' ','_').replace(':','_')
    
    # programmatically create a class equivalent to :
    # class Singleton_Sat_Jan__2_18_08_32_2016:
    #     def __init__(self): pass
    #     def value(self, x): return fj(x)
    
    def __init__(self): pass
    def value(self, x): return jitted_fun(x)
    SingletonClass = type(classname, (object,), {'__init__': __init__, 'value': value})
    
    # jit compile the class
    # spec is [] since we don't store attributes
    spec = []
    sc = jitclass(spec)(SingletonClass)
    
    # return a unique instance of the class
    return sc()


if __name__ == "__main__":

    from numba import njit


    @fjit
    def f(x):
        return x**2


    # f is now a "jitted" function (wrapped in a class)
    f.value(3.)



    from numpy import linspace
    @njit
    def function_of_a_function(f,x,N):
        xvec = linspace(0,x,N)
        t = 0.0
        for i in range(N):
            t += f.value(xvec[i])
        return t/N


    function_of_a_function(f, 1, 10000)
