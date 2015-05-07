# Assume that f_source and g_source are two functions defined in an external
# file funlib.py

# This example shows how to compile the function g_source, without modifying the
# external file.

from funlib import f_source, g_source

from numba import jit


# Compiling f_source alone is not a problem:
test = jit(nopython=True)(f_source)(0.5)
print("OK : {}".format(test))


# The problem arises when cmopiling g_source which calls f_source
try:
    resp = jit(nopython=True)(g_source)(1.0)
except:
    # attempt fails because no jitted version of f_source is available
    # when compiling g_source
    pass


# Note that:
# g_source=jit(nopython=True)(g_source)
# f_source=jit(nopython=True)(f_source)
# would not work either.
# The problem comes from the fact that the f_source function object holds
# references to the original f_source function:

assert( 'f_source' in f_source.func_globals )

# One solution consists in copying the sourcecode of g_source (or f_source)
# and reevaluating in a new context which can be manipulated and where functions
# can be jitted. Note that any external reference, like module-wide imports
# are lost in the process.


def jit_in_context(fun, d, *args, **kwargs):

    # to get an AST of fun, without reference to initial module
    import ast
    import inspect
    source = inspect.getsource(fun)
    tree = ast.parse(source)
    name = tree.body[0].name

    # eval the AST in context d
    code = compile(tree, "<string>", 'exec')
    eval(code, d)

    # jit the function in context d
    fun = d[name]
    jitted_fun = jit(fun, *args, **kwargs)
    d[name] = jitted_fun

    return jitted_fun



# Exemple:

# the next functions takes a function g, which depends on a function f
# and returns the copmpiled function g

def factory(f,g, *args, **kwargs):
    d = {}
    jit_in_context(f_source, d, *args, **kwargs)
    myfun = jit_in_context(g_source,  d, *args, **kwargs)
    return myfun


resp = factory(f_source, g_source, nopython=True)(1.0)

print("Success: g(f(1.0))={}".format(resp))
