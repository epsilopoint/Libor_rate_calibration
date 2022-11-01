import matplotlib.pyplot as plt
import numpy as np
import math as mt
import pandas as pd


df = pd.read_excel('Libor_rate.xlsx.',engine = 'openpyxl')
"""
We will be use exel file with Libor rates data from 01-01-2000 up to 12-01-2021
"""

r,t=[],[]

def MC_simulation(S0,lmb,mu,sigma,T,N):
    """
    Use Vasicek model to make Stochastic modelling. Next value is summ of previous value with adding calculated avareged 
    value and summation with stochastic part. it will return a the resulting model with a time step delta_t
    """
    Nml=[]
    Nml=np.random.normal(0, 1, N)
    r.append(S0)
    t.append(0)
    delta_t=T/N
    for i in range(N-1):
        t.append(t[i]+delta_t)
    for i in range(N-1):
        r.append(r[i]+lmb*(mu-r[i])+sigma*(np.sqrt(delta_t)*Nml[i]))
    plt.plot(t, r, "r-.", lw=3, alpha=0.6)
    plt.title("Simmulation")
    return r,t



def Callibration(T,r):
    """
    We will use methods which was proposed by Thijs van den Berg  in Calibrating the Ornstein-Uhlenbeck(Vasicek) model 
    to make estimation on th avareged step value mu, speed of reversion lmb and stochastic parametr sigma.
    """
    N=len(r)
    delta_t=T/N
    S_x,S_y,S_xx,S_yy,S_xy,lmb=0,0,0,0,0,0
    lmb,a,b,mu,sigma=0,0,0,0,0
    for i in range(N):
        S_x=S_x+r[i]
        S_xx=S_xx+r[i]*r[i]
    for j in range(N-1):
        S_y=S_y+r[j+1]
        S_yy=S_yy+r[j+1]*r[j+1]
        S_xy=S_xy+r[j]*r[j+1]
    a=(N*S_xy-S_x*S_y)/(N*S_xx-S_x*S_x)
    b=(S_y-a*S_x)/N
    sd_epsilon=np.sqrt((N*S_yy-S_y*S_y-a*(N*S_xy-S_x*S_y))/(N*(N-2)))
    lmb=-mt.log(a)/delta_t
    mu=b/(1-a)
    sigma=sd_epsilon*mt.sqrt((-2*mt.log(a))/(delta_t*(1-a*a)))
    return lmb,mu,sigma
s=df['Libor rates, 12m']    

lmb,mu,sigma=Callibration(20, s)
S0=s[0]
N=len(s)
delta_t=20/N
print(N)
MC_simulation(S0,lmb,mu,sigma,20,N)
t=[]
t.append(0)
for i in range(N-1):
    t.append(t[i]+delta_t)
plt.plot(t, s, "b-.", lw=3, alpha=0.6)
plt.title("Simmulation")
plt.show()

    

    

    
    
    
    
    
