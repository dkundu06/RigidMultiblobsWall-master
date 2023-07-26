import numpy as np
import math 
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline


time_step=[2.5, 3, 4, 5]
lin_vel=[0.0075, 0.005, 0.002, 0.0012]
ang_vel=[0.001, 0.0009, 0.0007, 0.0005]

# time_step=[2.5, 3, 4, 5]
# lin_vel=[1.21033, 1.16946, 1.12801, 1.100932]
# ang_vel=[0.16642, 0.11527, 0.0666, 0.04238]

time_step=np.array(time_step)
lin_vel=np.array(lin_vel)
ang_vel=np.array(ang_vel)


X_Y_Spline1 = make_interp_spline(time_step, lin_vel)
X_Y_Spline2 = make_interp_spline(time_step, ang_vel)

Lom1=lin_vel.copy()
Lom2=ang_vel.copy()
 
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(time_step.min(), time_step.max(), 500)
Y1_ = X_Y_Spline1(X_)
Y2_ = X_Y_Spline2(X_)



fig, ax = plt.subplots()
#plt.plot(X_, Y1_, "r",label = "Linear velocity")
#plt.plot(X_, Y2_, "g",label = "Angular velocity")

plt.plot(X_, Y1_, "r",label = "velocity in X-direction (Vx)")
plt.plot(X_, Y2_, "g",label = "Oseen velocity")
#plt.plot(time_step, Lom1, "ko",label = "Maxey and Patel (2001)")
#plt.plot(time_step, Lom2, "rd",label = "Maxey and Patel (2001)")
#plt.plot(time_step,lin_vel,"r",label = "linear velocity")
#plt.plot(time_step,ang_vel,"g",label = "angular velocity")
ax.set_xlabel(r'$r/a$', fontsize = 18)
#ax.set_ylabel(r'$v/w$', fontsize=18)
ax.set_ylabel(r'$v_x$', fontsize=18)
#ax.set_ylabel(r'$\Omega$', fontsize=18)
plt.legend(loc = 0)
# plt.xlim(1.9, 12.1)
# plt.ylim(1, 1.6)
plt.show()
