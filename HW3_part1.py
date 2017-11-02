# nonlinear pendulum d^2 theta /dt^2 + omega_0^2 sin(theta) = 0 
# omega_0^2 is defined as g/length
"""
This code solves the differential equation for the nonlinear pendulum
and
plots it

@author: drew bischel
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib import rc, rcParams
import matplotlib as mpl

def pi_constrain(theta):
    
    for i in range(len(theta)):
        if theta[i] >= np.pi:
            theta[i:] = theta[i:] - 2*np.pi
        elif theta[i] <= -np.pi:
            theta[i:] = theta[i:] + 2*np.pi
        else:
            continue
    return theta

def deriv(th, t0):
    a = 30.0 # = g/length
    return np.array([th[1], -a*np.sin(th[0])])
    
def d(th_d, time):
    a = 9.8 # = g/length
    k = 1.0 # friction coefficient
    F_d = 1.5 # driving force
    W_drive = 2.0 # driving frequency
    return np.array((
                     -a*np.sin(th_d[1]) - k*th_d[1] + F_d*np.sin(W_drive*time),  # th_d[0]' (=th_d'')
                     th_d[0]                                         # th_d[1]' (=th_d')
                   ))
                       
time = np.arange(0, 6.78, 0.001)
# w_guess = 10.954450988530306
# w = 10.954451150103322
th_initial = np.array([0, 10.95445098853030695]) # [thet_0, w_0] timestep :0.01 sec -> w0 = 10.9544509896144299785
th = odeint(deriv, th_initial, time)
w = th[:, 1]
theta = th[:, 0]
theta = pi_constrain(theta)

time2 = np.arange(0, 4.0, 0.001)
th_initial2 = np.array([0.0, 10.0]) # [thet_0, w_0] timestep :0.01 sec -> w0 = 10.9544509896144299785
th2 = odeint(deriv, th_initial2, time2)
w2 = th2[:, 1]
theta2 = th2[:, 0]
theta2 = pi_constrain(theta2)




font1 = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'bold',
        'size'   : 11,
        }
        
font2 = {'family' : 'serif',
        'color'  : 'black',
        'weight' : 'normal',
        'size'   : 16,
        }


mpl.rcParams['font.size'] = 11.
mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['axes.labelsize'] = 11.
mpl.rcParams['xtick.labelsize'] = 11.
mpl.rcParams['ytick.labelsize'] = 11.

fig = plt.figure()
fig.suptitle('Non-linear pendulum', fontdict = font2)

plt.subplot(2, 2, 1)
plt.plot(time2, theta2, 'o', markersize=1)
plt.title('a)', loc = 'left', fontdict = font1)
plt.xlabel(r'$t$', fontsize=16)
plt.ylabel(r'$\theta (t)$', fontsize=16)
plt.xticks( np.arange(5) )
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'-$\pi$', r'-$\pi/2$', r"$0$", r'$\pi/2$',r'$\pi$'])
plt.grid(True)

plt.subplot(2, 2, 2)
plt.plot(theta2, w2, '.', markersize=2)
plt.xlabel(r'$\theta (t)$', fontsize=16)
plt.ylabel(r'$\omega (t)$', fontsize=16)
plt.title('b)', loc = 'left', fontdict = font1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'-$\pi$', r'-$\pi/2$', r"$0$", r'$\pi/2$',r'$\pi$'])
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(time, theta, 'o', markersize=1)
plt.xlabel(r'$t$', fontsize=16)
plt.ylabel(r'$\theta (t)$', fontsize=16)
plt.title('c)', loc = 'left', fontdict = font1)
plt.yticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'-$\pi$', r'-$\pi/2$', r"$0$", r'$\pi/2$',r'$\pi$'])
plt.grid(True)

plt.subplot(2, 2, 4)
plt.plot(theta, w, '.', markersize=2)
plt.xlabel(r'$\theta (t)$', fontsize=16)
plt.ylabel(r'$\omega (t)$', fontsize=16)
plt.title('d)', loc = 'left', fontdict = font1)
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'-$\pi$', r'-$\pi/2$', r"$0$", r'$\pi/2$',r'$\pi$'])
plt.grid(True)


plt.show()
