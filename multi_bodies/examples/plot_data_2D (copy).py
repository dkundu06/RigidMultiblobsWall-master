import numpy as np
import math 
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline



#time_step=[2, 3, 4, 4.5, 5]
#time_step=100*time_step
#our_vel=[0.1, 0.05847, 0.0334, 0.026, 0.02143]
#ang_vel=[0.156, 0.076, 0.048, 0.0385, 0.033]


time_step=[2.5, 3, 4, 4.5, 5]
theta_0=[0.0075, 0.004, 0.002, 0.0016, 0.0012]
theta_90=[0.0, 0.0, 0.0, 0.0, 0.0]
theta_45=[-0.17055, -0.1544, -0.1252, -0.11, -0.102514]
theta_n135=[-0.17055, -0.1544, -0.1252, -0.11, -0.102514]
theta_135=[0.172, 0.1563, 0.1252, 0.11, 0.102514]
theta_n45=[0.172, 0.1563, 0.1252, 0.11, 0.102514]
theta_60=[-0.146, -0.13257, -0.10725, -0.09, -0.08833]
theta_n60=[0.146, 0.13257, 0.10725, 0.09, 0.08833]

theta_OSS45=[-0.02, -0.0184, -0.0165, -0.015, -0.0145]
theta_OSS60=[-0.01526, -0.015, -0.0135, -0.0127, -0.012]

theta_OSS90=[0.0, 0.0, 0.0, 0.0, 0.0]
##########################################################################################

new_time_step=[2.5, 3, 4, 4.5, 5, 10, 15, 20, 25, 30, 40, 50]
new_theta_45=[-0.17055, -0.1544, -0.1252, -0.1129, -0.102514, -0.05306, -0.0356, -0.0267, -0.02145, -0.01788, -0.0134, -0.010738]
new_theta_OSS45=[-0.02, -0.0183, -0.016505, -0.0148, -0.0138, -0.00864, -0.00608, -0.00468, -0.003806, -0.0032, -0.00243, -0.001962]




#########################################################################################
#time_step=100*time_step
our_vel_27=[2.499706442378513138e-01, 1.176257923889418884e-01, 6.688071884276247658e-02, 4.291366949803619713e-02]
our_vel_125=[2.492146937347103353e-01, 1.178257923889418884e-01, 6.688071884276247658e-02, 4.291366949803619713e-02]
our_vel_343=[2.491028826614212210e-01, 1.176643908487703394e-01, 6.686560234658144031e-02, 4.290851497629022404e-02]
our_vel_1000=[2.493469560327499224e-01, 1.175643908487703394e-01, 6.686560234658144031e-02, 4.290851497629022404e-02]
our_vel_3375=[2.494974079971246095e-01, 1.177257923889418884e-01, 6.688071884276247658e-02, 4.291366949803619713e-02]

time_step=np.array(time_step)
#ang_vel=np.array(ang_vel)
our_vel_27=np.array(our_vel_27)
our_vel_125=np.array(our_vel_125)
our_vel_343=np.array(our_vel_343)
our_vel_1000=np.array(our_vel_1000)
our_vel_3375=np.array(our_vel_3375)

theta_0=np.array(theta_0)
theta_90=np.array(theta_90)
theta_45=np.array(theta_45)
theta_n135=np.array(theta_n135)
theta_n45=np.array(theta_n45)
theta_60=np.array(theta_60)
theta_n60=np.array(theta_n60)
theta_135=np.array(theta_135)
theta_OSS45=4.63*np.array(theta_OSS45)
theta_OSS60=4.63*np.array(theta_OSS60)

###############################################################################
new_time_step=np.array(new_time_step)
new_theta_45=np.array(new_theta_45)
new_theta_OSS45=4.63*np.array(new_theta_OSS45)
divide=np.divide(new_theta_45,new_theta_OSS45)
print(divide)


#################################################################################



# X_Y_Spline1 = make_interp_spline(time_step, our_vel_27)
# X_Y_Spline2 = make_interp_spline(time_step, our_vel_125)
# #X_Y_Spline22 = make_interp_spline(time_step, ang_vel1)
# X_Y_Spline3 = make_interp_spline(time_step, our_vel_343)
# X_Y_Spline4 = make_interp_spline(time_step, our_vel_1000)
# X_Y_Spline5 = make_interp_spline(time_step, our_vel_3375)



X_Y_Spline1 = make_interp_spline(time_step, theta_0)
X_Y_Spline2 = make_interp_spline(time_step, theta_90)
X_Y_Spline3 = make_interp_spline(time_step, theta_45)
X_Y_Spline4 = make_interp_spline(time_step, theta_n45)
X_Y_Spline5 = make_interp_spline(time_step, theta_n135)
X_Y_Spline6 = make_interp_spline(time_step, theta_60)
X_Y_Spline7 = make_interp_spline(time_step, theta_n60)
X_Y_Spline8 = make_interp_spline(time_step, theta_135)
X_Y_Spline9 = make_interp_spline(time_step, theta_OSS45)
X_Y_Spline10 = make_interp_spline(time_step, theta_OSS60)

#####################################################################################
X_Y_Spline20 = make_interp_spline(new_time_step, new_theta_45)
X_Y_Spline21 = make_interp_spline(new_time_step, divide)

divide2=[1.85179, 1.8422, 1.69835, 1.64759, 1.60443, 1.32639, 1.26463, 1.232209, 1.21724, 1.206803, 1.191015, 1.18207]
X_Y_Spline22 = make_interp_spline(new_time_step, divide2)
#####################################################################################




#Lom1=our_vel.copy()
#Lom2=ang_vel.copy()
 
# Returns evenly spaced numbers
# over a specified interval.
X_ = np.linspace(time_step.min(), time_step.max(), 500)
Y1_ = X_Y_Spline1(X_)
Y2_ = X_Y_Spline2(X_)
# #Y22_ = X_Y_Spline22(X_)
Y3_ = X_Y_Spline3(X_)
Y4_ = X_Y_Spline4(X_)
Y5_ = X_Y_Spline5(X_)
Y6_ = X_Y_Spline6(X_)
Y7_ = X_Y_Spline7(X_)
Y8_ = X_Y_Spline8(X_)
Y9_ = X_Y_Spline9(X_)
Y10_ = X_Y_Spline10(X_)

#################################################################################
X0_ = np.linspace(new_time_step.min(), new_time_step.max(), 500)
Y20_ = X_Y_Spline20(X0_)
Y21_ = X_Y_Spline21(X0_)
Y22_ = X_Y_Spline22(X0_)
#################################################################################



# fig, ax = plt.subplots()
# plt.plot(X_, Y1_, "r",label = r'$\Theta=0^\circ$')
# plt.plot(X_, Y3_, "b",label = r'$\Theta=45^\circ$')
# plt.plot(X_, Y6_, "g",label = r'$\Theta=60^\circ$')
# plt.plot(X_, Y2_, "--",label = r'$\Theta=90^\circ$')
# #plt.plot(X_, Y8_, "m",label = r'$\Theta=135^\circ$')
# #plt.plot(X_, Y7_, "c",label = r'$\Theta=-60^\circ$')
# #plt.plot(time_step, theta_n45, "d",label = r'$\Theta=-45^\circ$')
# #plt.plot(time_step, theta_n135, "o",label = r'$\Theta=-135^\circ$')
# plt.plot(X_, Y9_, "--",label = " $\Theta=45^\circ$ (Ossen prediction)")
# plt.plot(X_, Y10_, "--",label = " $\Theta=60^\circ$ (Ossen prediction)")
# plt.plot(time_step, theta_OSS90, "o",label = ' $\Theta=0^\circ$ (Ossen prediction)')
# # plt.plot(X_, Y5_, "r",label = "27 blobs")

# # plt.plot(time_step, our_vel_125, "cd",label = "125 blobs")
# # plt.plot(time_step, our_vel_343, "bo",label = "343 blobs")
# # plt.plot(time_step, our_vel_1000, "ks",label = "1000 blobs")
# # plt.plot(time_step, our_vel_3375, "m*",label = "3375 blobs")
# #plt.plot(X_, Y22_, "g--",label = "Lomholt and Maxey (2003) by 2")
# #plt.plot(X_, Y2_, "r",label = "125 blobs")
# #plt.plot(X_, Y3_, "b",label = "343 blobs")
# #plt.plot(X_, Y4_, "k",label = "1000 blobs")
# #plt.plot(X_, Y5_, "m",label = "3375 blobs")
# #plt.plot(time_step, Lom1, "ko",label = "Maxey and Patel (2001)")
# #plt.plot(time_step, Y2_, "rd",label = "Maxey and Patel (2001)")
# #plt.plot(time_step,lin_vel,"r",label = "linear velocity")
# #plt.plot(time_step,ang_vel,"g",label = "angular velocity")
# ax.set_xlabel(r'$r/a$', fontsize = 18)
# ax.set_ylabel(r'$V_x$ ($\mu$m/s)', fontsize=18)
# plt.legend(loc = 4)
# #plt.xlim(1.5, 5.5)
# plt.ylim(-0.25, 0.03)
# plt.show()


fig, ax = plt.subplots()
#plt.plot(new_time_step, new_theta_45, "o",label = ' $\Theta=45^\circ$ (Numerical)')
plt.plot(X0_, Y20_, "k",label = ' $\Theta=45^\circ$ (Numerical)')
plt.plot(new_time_step, new_theta_OSS45, "o",label = ' $\Theta=45^\circ$ (Oseen prediction)')
#plt.plot(X0_, Y21_, "r",label = ' $\Theta=45^\circ$ (Oseen)')
#plt.plot(X0_, Y22_, "--",label = ' $\Theta=45^\circ$ (Ratio of Numerical and Oseen prediction)')
#plt.plot(new_time_step, divide, "o",label = ' $\Theta=45^\circ$ (Oseen)')
ax.set_xlabel(r'$r/a$', fontsize = 18)
ax.set_ylabel(r'$V_x$ ($\mu$m/s)', fontsize=14)
plt.legend(loc = 5)
#plt.xlim(1.5, 5.5)
#plt.ylim(1.1, 2)
plt.show()



