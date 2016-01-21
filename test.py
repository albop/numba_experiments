import time
import numpy

## prepare the problem

d = 3       # number of dimensions
K = 50      # number of points along each dimension
N = 10**6  # number of points at which to evaluate splines
T = 10      # number of repetitions (to cancel effect of transfer times)

dtype = numpy.float64

a = numpy.array([0.0,0.0,0.0],dtype=dtype)
b = numpy.array([1.0,1.0,1.0],dtype=dtype)
orders = numpy.array([K,K,K],dtype=numpy.int32)
#
# random coefficients
C = numpy.random.random(orders+2)
C = C.astype(dtype)

X = numpy.random.random((N,3))*0.5+0.5
X = X.astype(dtype)
res = numpy.zeros(N,dtype=dtype)
res2 = res.copy()



from numba import cuda
from eval_cubic_cuda import vec_eval_cubic_spline_3 as original
from eval_cubic_cuda import Ad,dAd

Ad = Ad.astype(dtype)
dAd = dAd.astype(dtype)

jitted = cuda.jit(original)

res_cuda = numpy.zeros_like(res)

d_a = cuda.to_device(a)
d_b = cuda.to_device(b)
d_orders = cuda.to_device(orders)
d_C = cuda.to_device(C)
d_Ad = cuda.to_device(Ad)
d_dAd = cuda.to_device(dAd)
d_X = cuda.to_device(X)
d_res_cuda = cuda.to_device(res_cuda)

#warmup
jitted[int(N/512)+1, 512](d_a,d_b,d_orders,d_C,d_X,d_res_cuda,d_Ad,d_dAd)

cuda.synchronize()
t1 = time.time()
for t in range(T):
    jitted[int(N/512)+1, 512](d_a,d_b,d_orders,d_C,d_X,d_res_cuda,d_Ad,d_dAd)
cuda.synchronize()
t2 = time.time()
res_cuda = d_res_cuda.copy_to_host()

print("CUDA: {}" .format((t2-t1)/T))


# Compare with CPU impplementations (requires interpolation.py)

from interpolation.splines.eval_cubic_numba import vec_eval_cubic_spline_3

vec_eval_cubic_spline_3(a,b,orders,C,X,res)

t1 = time.time()
for t in range(T):
    vec_eval_cubic_spline_3(a,b,orders,C,X,res)
t2 = time.time()


print("Cubic (CPU): {}".format((t2-t1)/T))
# print("Linear (CPU): {}".format((t3-t2)/T))

# check that cuda and CPU give the same result
assert( abs(res_cuda - res).max()<1e-8 )
