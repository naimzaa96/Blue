#Known Variables and initial values
M = 100 # mass of both objects in kg
A = 0.1 # cross-sectional area of objects in m^2
y_0 = 10**(3.5) # intial drop height in m
vx_0 = 10 # initial horizontal launch velocity in m/s
C = 0.5 # drag coefficient which is unitless
rho = 1.225 # density of medium in kg/m^3
B_2 = .5*A*(C)*(rho)/M # combined drag cofficient devided by mass
dt = 0.01 # in seconds
time = 30 #in seconds
g = 9.8 # m/s^2
n_steps = math.ceil(time/dt)


#create arrays for position, velocity and Drag force of projectile 1
y_1  = np.zeros(n_steps) 
V_y1 = np.zeros(n_steps)
F_d1 = np.zeros(n_steps)

#create arrays for position and velocity of launched particle 2
x_2  = np.zeros([n_steps])
y_2  = np.zeros([n_steps])

V_x2 = np.zeros([n_steps]) 
V_y2 = np.zeros([n_steps]) 
V_2  = np.zeros([n_steps]) 

#run numerical calculation for dropped projectile
V_y1, T, y_1 = updateP_1(V_y1,y_1,F_d1,B_2,g, dt, y_0)

#run numerical calculation for trajectory (and other values) of the launched projectile
V_2, V_x2, V_y2, T_2, x_2, y_2 = updateP_2(vx_0, y_0, B_2, g, dt)

# graphs
#plot y-velocity for dropped particle as a function of time, to see if our drag is working as intended
#SPOILER ALERT: It is!
plotV1, = plt.plot(T, V_y1, linewidth = 4, color = 'cyan', label = 'Numerical V1')

# graph stuff
xlabel = plt.xlabel(r'time') 
ylabel = plt.ylabel('Vy')
plt.grid()
plt.legend(handles=[plotV1], loc='best')
plt.savefig('HW2_V1.png', bbox_inches='tight')

#plot y-velocity of second particle as a function of time to check if drag is working
#SPOILER ALERT: it is now!
plotV2, = plt.plot(T_2, V_y2, linewidth = 4, color = 'cyan', label = 'Numerical V2')

#graph stuff
xlabel = plt.xlabel(r'time') 
ylabel = plt.ylabel('Velocity')
plt.grid()
plt.legend(handles=[plotV2], loc='best')
plt.savefig('HW2_V2.png', bbox_inches='tight')

#create and save an ascii table for position and time values of the launched projectile with respect to the ground
from astropy.table import Table, Column, MaskedColumn, MaskedColumn
resultstable = Table([np.round(T_2, 3), np.round(x_2,3), np.round(y_2,3)], names=['t (sec)','x (m)', 'y (m)'])

ascii.write(resultstable,'CalderNaimzadeh-PHYS486-HW2.tbl' , delimiter = '\t', overwrite = True)
resultstable

#check values against professor's values for t=3s
# Coveys values for t=3:
# x = 29.598, y=3118.675
print(T_2[300], 'seconds ', x_2[300], 'meters ', y_2[300], 'meters')
#they look pretty good!

#now need to calculate time difference for various changes in parameters

#create arrays of different parameters
  #changing mass by a factor of two changes B_2 by a factor of 1/2
  #changing drag coefficient by a factor of two changes B_2 by a factor of 2
    #B_2 can contain both of these parameters, need to vary over 5-7 powers of 10
  #changing launch speed has a different effect
  #changing initial height has a different effect
    #these two parameters can not be combined
# Varying C/M, which affects B_2
#create two arrays, one to store the time difference values which are affiliated manipulating 
#the parameter C/M (B_2)
timeDifference = np.zeros(5000)
CMarray =np.zeros(5000)

for t in range(0,5000):
  #store outputs of update function for projectile 1
  #changes B_2 every iteration by a step of 0.1
  data = updateP_1(V_y1, y_1, F_d1, (t/10)*B_2, g, dt, y_0)
  
  #store the y position and time for projectile 1
  massDrag01_y1 = data[2]
  massDrag01_T1 = data[1]
  
  #update array of C/M's
  CMarray[t] = (t/10)*B_2
  
  #Similar to above for projectile 2
  data2 = updateP_2(vx_0, y_0, (t/10)*B_2, g, dt)
  
  massDrag01_x2 = data2[4]
  massDrag01_y2 = data2[5]
  massDrag01_T2 = data2[3]
  
  #update time difference array by taking the difference between landing times of each iteration
  timeDifference[t] = interp_2(massDrag01_T2, massDrag01_x2, massDrag01_y2)[0] - interp_0(massDrag01_T1, massDrag01_y1)
  
  
#plot time difference vs C/M's
plotCMdiff, = plt.plot(np.linspace(0,2000,2000)*0.1, timeDifference[:2000], linewidth = 4, color = 'cyan', label = 'Numerical V2')


#graph stuff
xlabel = plt.xlabel(r'$\frac{C}{M}$ in units of $\frac{C_0}{M_0}$') 
ylabel = plt.ylabel('Difference in Landing Times [s]')
plt.grid()
plt.savefig('HW2_CMs.png', bbox_inches='tight')

#Similar to above, but for varying the launch height
timeDifference_y0 = np.zeros(300)
y0array =np.zeros(300)

for t in range(0,300):
  #varying y_0 in steps of 0.01 times the initial value
  data = updateP_1(V_y1, y_1, F_d1, B_2, g, dt, (t/100)*y_0)
  
  height_y1 = data[2]
  height_T1 = data[1]
  
  #updates y_0array up to 3 times the initial launch height
  y0array[t] = (t/100)*y_0
  
  data2 = updateP_2(vx_0, (t/100)*y_0, B_2, g, dt)
  
  height_x2 = data2[4]
  height_y2 = data2[5]
  height_T2 = data2[3]
  
  timeDifference_y0[t] = interp_2(height_T2, height_x2, height_y2)[0] - interp_0(height_T1, height_y1)

ploty0diff, = plt.plot(np.linspace(0,300,300)*0.01*y_0, timeDifference_y0, linewidth = 4, color = 'cyan', label = 'Numerical V2')


#graph stuff
xlabel = plt.xlabel(r'Launch Height [m]') 
ylabel = plt.ylabel('Difference in Landing Times [s]')
plt.grid()
plt.savefig('HW2_y0s.png', bbox_inches='tight')


#calculate values for initial velocity from 0-10 m/s (0-vx0)
timeDifference_vx01 = np.zeros(100)
vx0array1 =np.zeros(100)
for t in range(0,100):
  
  data = updateP_1(V_y1, y_1, F_d1, B_2, g, dt, y_0)
  
  vel_y1 = data[2]
  vel_T1 = data[1]
  
  vx0array1[t] = (t/100)*vx_0
  
  data2 = updateP_2((t/100)*vx_0, y_0, B_2, g, dt)
  
  vel_x2 = data2[4]
  vel_y2 = data2[5]
  vel_T2 = data2[3]
  
  timeDifference_vx01[t] = interp_2(vel_T2, vel_x2, vel_y2)[0] - interp_0(vel_T1, vel_y1)


#calculate values for initial velocity from 0-100 m/s
timeDifference_vx02 = np.zeros(1000)
vx0array2 =np.zeros(1000)
for t in range(0,1000):
  
  data = updateP_1(V_y1, y_1, F_d1, B_2, g, dt, y_0)
  
  vel_y1 = data[2]
  vel_T1 = data[1]
  
  vx0array2[t] = (t/10)*vx_0
  
  data2 = updateP_2(((t/10)*vx_0), y_0, B_2, g, dt)
  
  vel_x2 = data2[4]
  vel_y2 = data2[5]
  vel_T2 = data2[3]
  
  timeDifference_vx02[t] = interp_2(vel_T2, vel_x2, vel_y2)[0] - interp_0(vel_T1, vel_y1)

plt.figure(figsize = (20,10))

#left subplot: 0-10 m/s
plt.subplot(121)
plotvx0diff1 = plt.plot(np.linspace(0,10,100), timeDifference_vx01, linewidth = 4, color = 'cyan', label = '')
ylabel = plt.ylabel('Difference in Landing Times [s]')
xlabel = plt.xlabel(r'Launch velocity [m/s]')
plt.grid()

#middle subplot: 10-100 m/s
plt.subplot(122)
plotvx0diff2 = plt.plot(np.linspace(10,110,1000), timeDifference_vx02, linewidth = 4, color = 'cyan')
# plt.xlim(15,)
xlabel = plt.xlabel(r'Launch velocity [m/s]')
ylabel = plt.ylabel('Difference in landing times [s]')
plt.grid()

#save figure
plt.savefig('HW2_Vx0s.png', bbox_inches='tight')

#0-1 behaviour is cconcave up, 10+ behaviour is Concave down
#maybe use a figure of 3 plots highlighting each type of behaviour?

#now need to check how timestep effects the trajectories (numerical analysis)
#plot delta t for 'original' dropped/launched particles for different timesteps?
#plot v_y for different timesteps?
#need t1, y1; t2, x2, y2 for interpolate functions

#create arrays to store data for each timestep
V_y1_10 = np.zeros(n_steps)
T_10 = np.zeros(n_steps)
y1_10 = np.zeros(n_steps)

V_y1_100 = np.zeros(n_steps)
T_100 = np.zeros(n_steps)
y1_100 = np.zeros(n_steps)

V_y1_01 = np.zeros(n_steps)
T_01 = np.zeros(n_steps)
y1_01 = np.zeros(n_steps)

V_y2_10 = np.zeros(n_steps)
T_2_10 = np.zeros(n_steps)
x_2_10 = np.zeros(n_steps)
y_2_10 = np.zeros(n_steps)

V_y2_100 = np.zeros(n_steps)
T_2_100 = np.zeros(n_steps)
x_2_100 = np.zeros(n_steps)
y_2_100 = np.zeros(n_steps)

V_y2_01 = np.zeros(n_steps)
T_2_01 = np.zeros(n_steps)
x_2_01 = np.zeros(n_steps)
y_2_01 = np.zeros(n_steps)

#calculate trajectory information for different timesteps
V_y1_10, T_10, y1_10 = updateP_1(V_y1, y_1, F_d1, B_2, g, 10*dt, y_0)
V_y1_100, T_100, y1_100 = updateP_1(V_y1, y_1, F_d1, B_2, g, 100*dt, y_0)
V_y1_300, T_300, y1_300 = updateP_1(V_y1, y_1, F_d1, B_2, g, 300*dt, y_0)
V_y1_01, T_01, y1_01 = updateP_1(V_y1, y_1, F_d1, B_2, g, 0.1*dt, y_0)

__, __, V_y2_10, T_2_10, x_2_10, y_2_10 = updateP_2(vx_0, y_0, B_2, g, 10*dt)
__, __, V_y2_100, T_2_100, x_2_100, y_2_100 = updateP_2(vx_0, y_0, B_2, g, 100*dt)
__, __, V_y2_300, T_2_300, x_2_300, y_2_300 = updateP_2(vx_0, y_0, B_2, g, 300*dt)
__, __, V_y2_01, T_2_01, x_2_01, y_2_01 = updateP_2(vx_0, y_0, B_2, g, 0.1*dt)

#calculate delta_t for different time steps
delta_t = interp_2(T_2, x_2, y_2)[0] - interp_0(T, y_1)
delta_t10 = interp_2(T_2_10, x_2_10, y_2_10)[0] - interp_0(T_10, y1_10)
delta_t100 = interp_2(T_2_100, x_2_100, y_2_100)[0] - interp_0(T_100, y1_100)
delta_t300 = interp_2(T_2_300, x_2_300, y_2_300)[0] - interp_0(T_300, y1_300)
delta_t01 = interp_2(T_2_01, x_2_01, y_2_01)[0] - interp_0(T_01, y1_01)

#print difference in landing times for launched/dropped particles for each timestep
print(delta_t01, delta_t, delta_t10, delta_t100, delta_t300)

#compare landing times and x positions of launched particle for different timesteps
print(interp_2(T_2_300, x_2_300, y_2_300), interp_2(T_2_100, x_2_100, y_2_100), interp_2(T_2_10, x_2_10, y_2_10), interp_2(T_2, x_2, y_2), interp_2(T_2_01, x_2_01, y_2_01))


#plot trajectories for different timesteps
ploty, = plt.plot(T_2, y_2, linewidth = 4, color = 'k', label = '0.01s')
ploty10, = plt.plot(T_2_10, y_2_10, linewidth = 4, color = 'cyan', label = '0.1s')
ploty100, = plt.plot(T_2_100, y_2_100, linewidth = 4, color = 'b', label = '1s')
ploty300, = plt.plot(T_2_300, y_2_300, linewidth = 4, color = 'g', label = '3s')


#graph stuff

xlabel = plt.xlabel(r'Time [s]') 
ylabel = plt.ylabel('Height [m]')
plt.legend(handles=[ploty, ploty10, ploty100, ploty300], loc='best')
plt.grid()
plt.savefig('HW2_timestep.png', bbox_inches='tight')

