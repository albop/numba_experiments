from __future__ import division

from numba import double, int64

from numba import jit, njit

import numpy as np
from numpy import zeros, array

from math import floor
from numpy import empty


Ad = array([
#      t^3       t^2        t        1
   [-1.0/6.0,  3.0/6.0, -3.0/6.0, 1.0/6.0],
   [ 3.0/6.0, -6.0/6.0,  0.0/6.0, 4.0/6.0],
   [-3.0/6.0,  3.0/6.0,  3.0/6.0, 1.0/6.0],
   [ 1.0/6.0,  0.0/6.0,  0.0/6.0, 0.0/6.0]
])

dAd = zeros((4,4))
for i in range(1,4):
    dAd[:,i] = Ad[:,i-1]*(4-i)


d2Ad = zeros((4,4))
for i in range(1,4):
    d2Ad[:,i] = dAd[:,i-1]*(4-i)

from numba import cuda


def vec_eval_cubic_spline_3(a, b, orders, coefs, points, out, Ad, dAd):

    d = a.shape[0]
    N = points.shape[0]

    n = cuda.grid(1)

    if n < N:
        
        x0 = points[n,0]
        x1 = points[n,1]
        x2 = points[n,2]

        M0 = orders[0]
        start0 = a[0]
        dinv0 = (orders[0]-1.0)/(b[0]-a[0])
        M1 = orders[1]
        start1 = a[1]
        dinv1 = (orders[1]-1.0)/(b[1]-a[1])
        M2 = orders[2]
        start2 = a[2]
        dinv2 = (orders[2]-1.0)/(b[2]-a[2])

        # normalize coordinates to t \in [0,1]
        u0 = (x0 - start0)*dinv0
        i0 = int( floor( u0 ) )
        i0 = max( min(i0,M0-2), 0 )
        t0 = u0-i0
        u1 = (x1 - start1)*dinv1
        i1 = int( floor( u1 ) )
        i1 = max( min(i1,M1-2), 0 )
        t1 = u1-i1
        u2 = (x2 - start2)*dinv2
        i2 = int( floor( u2 ) )
        i2 = max( min(i2,M2-2), 0 )
        t2 = u2-i2

        
        tp0_0 = t0*t0*t0;  tp0_1 = t0*t0;  tp0_2 = t0;  tp0_3 = 1.0;
        tp1_0 = t1*t1*t1;  tp1_1 = t1*t1;  tp1_2 = t1;  tp1_3 = 1.0;
        tp2_0 = t2*t2*t2;  tp2_1 = t2*t2;  tp2_2 = t2;  tp2_3 = 1.0;

        Phi0_0 = 0
        Phi0_1 = 0
        Phi0_2 = 0
        Phi0_3 = 0
        if t0 < 0:
            Phi0_0 = dAd[0,3]*t0 + Ad[0,3]
            Phi0_1 = dAd[1,3]*t0 + Ad[1,3]
            Phi0_2 = dAd[2,3]*t0 + Ad[2,3]
            Phi0_3 = dAd[3,3]*t0 + Ad[3,3]
        elif t0 > 1:
            Phi0_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t0-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi0_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t0-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi0_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t0-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi0_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t0-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi0_0 = (Ad[0,0]*tp0_0 + Ad[0,1]*tp0_1 + Ad[0,2]*tp0_2 + Ad[0,3]*tp0_3)
            Phi0_1 = (Ad[1,0]*tp0_0 + Ad[1,1]*tp0_1 + Ad[1,2]*tp0_2 + Ad[1,3]*tp0_3)
            Phi0_2 = (Ad[2,0]*tp0_0 + Ad[2,1]*tp0_1 + Ad[2,2]*tp0_2 + Ad[2,3]*tp0_3)
            Phi0_3 = (Ad[3,0]*tp0_0 + Ad[3,1]*tp0_1 + Ad[3,2]*tp0_2 + Ad[3,3]*tp0_3)

        Phi1_0 = 0
        Phi1_1 = 0
        Phi1_2 = 0
        Phi1_3 = 0
        if t1 < 0:
            Phi1_0 = dAd[0,3]*t1 + Ad[0,3]
            Phi1_1 = dAd[1,3]*t1 + Ad[1,3]
            Phi1_2 = dAd[2,3]*t1 + Ad[2,3]
            Phi1_3 = dAd[3,3]*t1 + Ad[3,3]
        elif t1 > 1:
            Phi1_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t1-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi1_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t1-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi1_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t1-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi1_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t1-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi1_0 = (Ad[0,0]*tp1_0 + Ad[0,1]*tp1_1 + Ad[0,2]*tp1_2 + Ad[0,3]*tp1_3)
            Phi1_1 = (Ad[1,0]*tp1_0 + Ad[1,1]*tp1_1 + Ad[1,2]*tp1_2 + Ad[1,3]*tp1_3)
            Phi1_2 = (Ad[2,0]*tp1_0 + Ad[2,1]*tp1_1 + Ad[2,2]*tp1_2 + Ad[2,3]*tp1_3)
            Phi1_3 = (Ad[3,0]*tp1_0 + Ad[3,1]*tp1_1 + Ad[3,2]*tp1_2 + Ad[3,3]*tp1_3)

        Phi2_0 = 0
        Phi2_1 = 0
        Phi2_2 = 0
        Phi2_3 = 0
        if t2 < 0:
            Phi2_0 = dAd[0,3]*t2 + Ad[0,3]
            Phi2_1 = dAd[1,3]*t2 + Ad[1,3]
            Phi2_2 = dAd[2,3]*t2 + Ad[2,3]
            Phi2_3 = dAd[3,3]*t2 + Ad[3,3]
        elif t2 > 1:
            Phi2_0 = (3*Ad[0,0] + 2*Ad[0,1] + Ad[0,2])*(t2-1) + (Ad[0,0]+Ad[0,1]+Ad[0,2]+Ad[0,3])
            Phi2_1 = (3*Ad[1,0] + 2*Ad[1,1] + Ad[1,2])*(t2-1) + (Ad[1,0]+Ad[1,1]+Ad[1,2]+Ad[1,3])
            Phi2_2 = (3*Ad[2,0] + 2*Ad[2,1] + Ad[2,2])*(t2-1) + (Ad[2,0]+Ad[2,1]+Ad[2,2]+Ad[2,3])
            Phi2_3 = (3*Ad[3,0] + 2*Ad[3,1] + Ad[3,2])*(t2-1) + (Ad[3,0]+Ad[3,1]+Ad[3,2]+Ad[3,3])
        else:
            Phi2_0 = (Ad[0,0]*tp2_0 + Ad[0,1]*tp2_1 + Ad[0,2]*tp2_2 + Ad[0,3]*tp2_3)
            Phi2_1 = (Ad[1,0]*tp2_0 + Ad[1,1]*tp2_1 + Ad[1,2]*tp2_2 + Ad[1,3]*tp2_3)
            Phi2_2 = (Ad[2,0]*tp2_0 + Ad[2,1]*tp2_1 + Ad[2,2]*tp2_2 + Ad[2,3]*tp2_3)
            Phi2_3 = (Ad[3,0]*tp2_0 + Ad[3,1]*tp2_1 + Ad[3,2]*tp2_2 + Ad[3,3]*tp2_3)

        out[n] = Phi0_0*(Phi1_0*(Phi2_0*(coefs[i0+0,i1+0,i2+0]) + Phi2_1*(coefs[i0+0,i1+0,i2+1]) + Phi2_2*(coefs[i0+0,i1+0,i2+2]) + Phi2_3*(coefs[i0+0,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+0,i1+1,i2+0]) + Phi2_1*(coefs[i0+0,i1+1,i2+1]) + Phi2_2*(coefs[i0+0,i1+1,i2+2]) + Phi2_3*(coefs[i0+0,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+0,i1+2,i2+0]) + Phi2_1*(coefs[i0+0,i1+2,i2+1]) + Phi2_2*(coefs[i0+0,i1+2,i2+2]) + Phi2_3*(coefs[i0+0,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+0,i1+3,i2+0]) + Phi2_1*(coefs[i0+0,i1+3,i2+1]) + Phi2_2*(coefs[i0+0,i1+3,i2+2]) + Phi2_3*(coefs[i0+0,i1+3,i2+3]))) + Phi0_1*(Phi1_0*(Phi2_0*(coefs[i0+1,i1+0,i2+0]) + Phi2_1*(coefs[i0+1,i1+0,i2+1]) + Phi2_2*(coefs[i0+1,i1+0,i2+2]) + Phi2_3*(coefs[i0+1,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+1,i1+1,i2+0]) + Phi2_1*(coefs[i0+1,i1+1,i2+1]) + Phi2_2*(coefs[i0+1,i1+1,i2+2]) + Phi2_3*(coefs[i0+1,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+1,i1+2,i2+0]) + Phi2_1*(coefs[i0+1,i1+2,i2+1]) + Phi2_2*(coefs[i0+1,i1+2,i2+2]) + Phi2_3*(coefs[i0+1,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+1,i1+3,i2+0]) + Phi2_1*(coefs[i0+1,i1+3,i2+1]) + Phi2_2*(coefs[i0+1,i1+3,i2+2]) + Phi2_3*(coefs[i0+1,i1+3,i2+3]))) + Phi0_2*(Phi1_0*(Phi2_0*(coefs[i0+2,i1+0,i2+0]) + Phi2_1*(coefs[i0+2,i1+0,i2+1]) + Phi2_2*(coefs[i0+2,i1+0,i2+2]) + Phi2_3*(coefs[i0+2,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+2,i1+1,i2+0]) + Phi2_1*(coefs[i0+2,i1+1,i2+1]) + Phi2_2*(coefs[i0+2,i1+1,i2+2]) + Phi2_3*(coefs[i0+2,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+2,i1+2,i2+0]) + Phi2_1*(coefs[i0+2,i1+2,i2+1]) + Phi2_2*(coefs[i0+2,i1+2,i2+2]) + Phi2_3*(coefs[i0+2,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+2,i1+3,i2+0]) + Phi2_1*(coefs[i0+2,i1+3,i2+1]) + Phi2_2*(coefs[i0+2,i1+3,i2+2]) + Phi2_3*(coefs[i0+2,i1+3,i2+3]))) + Phi0_3*(Phi1_0*(Phi2_0*(coefs[i0+3,i1+0,i2+0]) + Phi2_1*(coefs[i0+3,i1+0,i2+1]) + Phi2_2*(coefs[i0+3,i1+0,i2+2]) + Phi2_3*(coefs[i0+3,i1+0,i2+3])) + Phi1_1*(Phi2_0*(coefs[i0+3,i1+1,i2+0]) + Phi2_1*(coefs[i0+3,i1+1,i2+1]) + Phi2_2*(coefs[i0+3,i1+1,i2+2]) + Phi2_3*(coefs[i0+3,i1+1,i2+3])) + Phi1_2*(Phi2_0*(coefs[i0+3,i1+2,i2+0]) + Phi2_1*(coefs[i0+3,i1+2,i2+1]) + Phi2_2*(coefs[i0+3,i1+2,i2+2]) + Phi2_3*(coefs[i0+3,i1+2,i2+3])) + Phi1_3*(Phi2_0*(coefs[i0+3,i1+3,i2+0]) + Phi2_1*(coefs[i0+3,i1+3,i2+1]) + Phi2_2*(coefs[i0+3,i1+3,i2+2]) + Phi2_3*(coefs[i0+3,i1+3,i2+3])))
