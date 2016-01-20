from numexpr import evaluate

def arbitrage(m, s, x, y, M, S, X, Y, p, out):
    A_1_ = m[(..., 0)]
    A_2_ = m[(..., 1)]
    E_ = m[(..., 2)]
    k_1_ = s[(..., 0)]
    k_2_ = s[(..., 1)]
    b_f_ = s[(..., 2)]
    db_f_ = x[(..., 0)]
    p_f_ = x[(..., 1)]
    i_1_ = x[(..., 2)]
    i_2_ = x[(..., 3)]
    ew_1_ = x[(..., 4)]
    ew_2_ = x[(..., 5)]
    w_1_ = x[(..., 6)]
    w_2_ = x[(..., 7)]
    y_1_ = y[(..., 0)]
    y_2_ = y[(..., 1)]
    c_1_ = y[(..., 2)]
    c_2_ = y[(..., 3)]
    Phi_1_ = y[(..., 4)]
    Phi_2_ = y[(..., 5)]
    Phi_1__p_ = y[(..., 6)]
    Phi_2__p_ = y[(..., 7)]
    A_1__1_ = M[(..., 0)]
    A_2__1_ = M[(..., 1)]
    E__1_ = M[(..., 2)]
    k_1__1_ = S[(..., 0)]
    k_2__1_ = S[(..., 1)]
    b_f__1_ = S[(..., 2)]
    db_f__1_ = X[(..., 0)]
    p_f__1_ = X[(..., 1)]
    i_1__1_ = X[(..., 2)]
    i_2__1_ = X[(..., 3)]
    ew_1__1_ = X[(..., 4)]
    ew_2__1_ = X[(..., 5)]
    w_1__1_ = X[(..., 6)]
    w_2__1_ = X[(..., 7)]
    y_1__1_ = Y[(..., 0)]
    y_2__1_ = Y[(..., 1)]
    c_1__1_ = Y[(..., 2)]
    c_2__1_ = Y[(..., 3)]
    Phi_1__1_ = Y[(..., 4)]
    Phi_2__1_ = Y[(..., 5)]
    Phi_1__p__1_ = Y[(..., 6)]
    Phi_2__p__1_ = Y[(..., 7)]
    beta_ = p[(..., 0)]
    theta_ = p[(..., 1)]
    gamma_ = p[(..., 2)]
    psi_ = p[(..., 3)]
    delta_ = p[(..., 4)]
    rho_A_ = p[(..., 5)]
    rho_E_ = p[(..., 6)]
    min_b_ = p[(..., 7)]
    max_b_ = p[(..., 8)]
    a1_ = p[(..., 9)]
    a2_ = p[(..., 10)]
    xi_ = p[(..., 11)]
    sigma_A_1_ = p[(..., 12)]
    sigma_A_2_ = p[(..., 13)]
    sigma_E_ = p[(..., 14)]
    kmin_ = p[(..., 15)]
    kmax_ = p[(..., 16)]
    min_bb_ = p[(..., 17)]
    max_bb_ = p[(..., 18)]
    spmin_ = p[(..., 19)]
    spmax_ = p[(..., 20)]
    S_1_ = p[(..., 21)]
    S_2_ = p[(..., 22)]
    country_ = p[(..., 23)]
    zeta_ = p[(..., 24)]
    hom_ = p[(..., 25)]
    y_1_ = out[(..., 0)]
    y_2_ = out[(..., 1)]
    c_1_ = out[(..., 2)]
    c_2_ = out[(..., 3)]
    Phi_1_ = out[(..., 4)]
    Phi_2_ = out[(..., 5)]
    Phi_1__p_ = out[(..., 6)]
    Phi_2__p_ = out[(..., 7)]
    out_0 = out[(..., 0)]
    out_1 = out[(..., 1)]
    out_2 = out[(..., 2)]
    out_3 = out[(..., 3)]
    out_4 = out[(..., 4)]
    out_5 = out[(..., 5)]
    out_6 = out[(..., 6)]
    out_7 = out[(..., 7)]
    evaluate('((k_1_) ** (theta_)) * (exp(A_1_))', out=out_0)
    evaluate('((k_2_) ** (theta_)) * (exp(A_2_))', out=out_1)
    evaluate('((y_1_) - (i_1_) + b_f_) - ((p_f_) * (db_f_))', out=out_2)
    evaluate('((y_2_) - (i_2_)) - ((((b_f_) - ((p_f_) * (db_f_))) / (S_2_)) * (S_1_))', out=out_3)
    evaluate('a1_ + ((a2_) / ((1) - (xi_))) * (((i_1_) / (k_1_)) ** ((1) - (xi_)))', out=out_4)
    evaluate('a1_ + ((a2_) / ((1) - (xi_))) * (((i_2_) / (k_2_)) ** ((1) - (xi_)))', out=out_5)
    evaluate('(a2_) * (((i_1_) / (k_1_)) ** (-(xi_)))', out=out_6)
    evaluate('(a2_) * (((i_2_) / (k_2_)) ** (-(xi_)))', out=out_7)

def arbitrage_numba(m, s, x, y, M, S, X, Y, p, out):
    A_1_ = m[(0)]
    A_2_ = m[(1)]
    E_ = m[(2)]
    k_1_ = s[(0)]
    k_2_ = s[(1)]
    b_f_ = s[(2)]
    db_f_ = x[(0)]
    p_f_ = x[(1)]
    i_1_ = x[(2)]
    i_2_ = x[(3)]
    ew_1_ = x[(4)]
    ew_2_ = x[(5)]
    w_1_ = x[(6)]
    w_2_ = x[(7)]
    y_1_ = y[(0)]
    y_2_ = y[(1)]
    c_1_ = y[(2)]
    c_2_ = y[(3)]
    Phi_1_ = y[(4)]
    Phi_2_ = y[(5)]
    Phi_1__p_ = y[(6)]
    Phi_2__p_ = y[(7)]
    A_1__1_ = M[(0)]
    A_2__1_ = M[(1)]
    E__1_ = M[(2)]
    k_1__1_ = S[(0)]
    k_2__1_ = S[(1)]
    b_f__1_ = S[(2)]
    db_f__1_ = X[(0)]
    p_f__1_ = X[(1)]
    i_1__1_ = X[(2)]
    i_2__1_ = X[(3)]
    ew_1__1_ = X[(4)]
    ew_2__1_ = X[(5)]
    w_1__1_ = X[(6)]
    w_2__1_ = X[(7)]
    y_1__1_ = Y[(0)]
    y_2__1_ = Y[(1)]
    c_1__1_ = Y[(2)]
    c_2__1_ = Y[(3)]
    Phi_1__1_ = Y[(4)]
    Phi_2__1_ = Y[(5)]
    Phi_1__p__1_ = Y[(6)]
    Phi_2__p__1_ = Y[(7)]
    beta_ = p[(0)]
    theta_ = p[(1)]
    gamma_ = p[(2)]
    psi_ = p[(3)]
    delta_ = p[(4)]
    rho_A_ = p[(5)]
    rho_E_ = p[(6)]
    min_b_ = p[(7)]
    max_b_ = p[(8)]
    a1_ = p[(9)]
    a2_ = p[(10)]
    xi_ = p[(11)]
    sigma_A_1_ = p[(12)]
    sigma_A_2_ = p[(13)]
    sigma_E_ = p[(14)]
    kmin_ = p[(15)]
    kmax_ = p[(16)]
    min_bb_ = p[(17)]
    max_bb_ = p[(18)]
    spmin_ = p[(19)]
    spmax_ = p[(20)]
    S_1_ = p[(21)]
    S_2_ = p[(22)]
    country_ = p[(23)]
    zeta_ = p[(24)]
    hom_ = p[(25)]
    y_1_ = out[(0)]
    y_2_ = out[(1)]
    c_1_ = out[(2)]
    c_2_ = out[(3)]
    Phi_1_ = out[(4)]
    Phi_2_ = out[(5)]
    Phi_1__p_ = out[(6)]
    Phi_2__p_ = out[(7)]
    out_0 = out[(0)]
    out_1 = out[(1)]
    out_2 = out[(2)]
    out_3 = out[(3)]
    out_4 = out[(4)]
    out_5 = out[(5)]
    out_6 = out[(6)]
    out_7 = out[(7)]
    out[0] = ((k_1_) ** (theta_)) * (exp(A_1_))
    out[1] = ((k_2_) ** (theta_)) * (exp(A_2_))
    out[2] = ((y_1_) - (i_1_) + b_f_) - ((p_f_) * (db_f_))
    out[3] = ((y_2_) - (i_2_)) - ((((b_f_) - ((p_f_) * (db_f_))) / (S_2_)) * (S_1_))
    out[4] = a1_ + ((a2_) / ((1) - (xi_))) * (((i_1_) / (k_1_)) ** ((1) - (xi_)))
    out[5] = a1_ + ((a2_) / ((1) - (xi_))) * (((i_2_) / (k_2_)) ** ((1) - (xi_)))
    out[6] = (a2_) * (((i_1_) / (k_1_)) ** (-(xi_)))
    out[7] = (a2_) * (((i_2_) / (k_2_)) ** (-(xi_)))

from numpy import *


N = 10**7

m = array([ 0.,  0.,  0.])
s = array([ 3.6301792,  3.6301792,  0.       ])
x =  array([ 0.        ,  0.96      ,  0.29041434,  0.29041434,  1.18182501, 1.18182501,  1.18182501,  1.18182501])
y = array([ 1.47223934,  1.47223934,  1.18182501,  1.18182501,  0.08      ,   0.08      ,  1.        ,  1.        ])
p = array([  0.96      ,   0.3       ,   4.        ,   4.        ,
                       0.08      ,   0.9       ,   0.999     , -10.        ,
                      10.        ,  -0.02      ,   0.60341763,   0.2       ,
                       0.025     ,   0.05      ,   0.        ,   2.        ,
                      10.        , -10.        ,  10.        ,   1.        ,
                       1.        ,   1.        ,   1.        ,   1.        ,
                       0.        ,   1.        ])


s = s[None,:].repeat(N,axis=0)
x = x[None,:].repeat(N,axis=0)
y = y[None,:].repeat(N,axis=0)
m = m[None,:].repeat(N,axis=0)
M = m.copy()
S = s.copy()
Y = y.copy()
X = x.copy()
out = X.copy()


arbitrage(m,s,x,y,M,S,X,Y,p,out)

import time
t1 = time.time()
arbitrage(m,s,x,y,M,S,X,Y,p,out)
t2 = time.time()


print("numexpr: {}".format(t2-t1))
from numba import guvectorize, float64


gufun_cpu = guvectorize([(float64[:],)*10],'(a),(b),(c),(d),(a),(b),(c),(d),(e)->(c)', target='cpu')(arbitrage_numba)
gufun_cpu(m,s,x,y,M,S,X,Y,p,out)

t1 = time.time()
gufun_cpu(m,s,x,y,M,S,X,Y,p,out)
t2 = time.time()
print('gufun: {}'.format(t2-t1))


gufun_parallel = guvectorize([(float64[:],)*10],'(a),(b),(c),(d),(a),(b),(c),(d),(e)->(c)', target='parallel')(arbitrage_numba)
gufun_parallel(m,s,x,y,M,S,X,Y,p,out)

t1 = time.time()
gufun_parallel(m,s,x,y,M,S,X,Y,p,out)
t2 = time.time()
print('gufun: {}'.format(t2-t1))



