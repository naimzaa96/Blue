
#create function to interpolate T value for final y_1=0
#using interpolation equation from the "Computational Physics" pg 28 equation 2.21
def interp_0(T, y_1):
  r = -y_1[-2]/y_1[-1]
  impact_time = (T[-2] +r*T[-1]) / (r+1)
  
  return impact_time

# function to calculate trajectories for dropped projectile 1
def updateP_1(V_y1, y_1, F_d1, B_2, g, dt, height):
  #calculate number of steps
  n_steps = math.ceil(time/dt)
  
  #calculate list of time values for our given time span and steps
  T = np.linspace(0,time, n_steps)
  #create arrays for position, velocity and Drag force of projectile 1
  y_1  = np.zeros(n_steps) 
  V_y1 = np.zeros(n_steps)
  F_d1 = np.zeros(n_steps)
  
  # update arrays with calculated values for drag force, velocity and position from ground
  # using eulers stepping method
  for t in range(0,(n_steps-1)):
    y_1[0] = height
    
    if y_1[t] >= 0 :
      F_d1[t+1] = B_2*(V_y1[t]**2)
      V_y1[t+1] = V_y1[t] + (-g + (F_d1[t]))*dt
      y_1[t+1] = y_1[t] + V_y1[t]*dt
    else:
      break

  return V_y1[:t+1], T[:t+1], y_1[:t+1]
                


#define a function to interpolate the impact time and x-position for launched particle 2
def interp_2(T, x_2, y_2):
  r = -y_2[-2]/y_2[-1]
  impact_time = (T[-2] +r*T[-1]) / (r+1)
  impact_x = (x_2[-2] + r*x_2[-1]) / (r+1)
  
  return impact_time, impact_x
  

#define a function to calculate the trajectory of the launched projectile 2
def updateP_2(V_x0, height, B_2, g, dt):
    n_steps = math.ceil(time/dt)
    T_2 = np.linspace(0,time, n_steps) #gives us all time values correspong to a maximum time 
    
    #create arrays for accelerations, velocities, and positions in both the x and y directions
    a_dx2 = np.zeros_like(T_2)
    a_dy2 = np.zeros_like(T_2)
    
    V_x2 = np.zeros_like(T_2)
    V_y2 = np.zeros_like(T_2)
    V_2 = np.array(np.sqrt(np.square(V_x2)+np.square(V_y2)))
    
    x_2 = np.zeros_like(T_2)
    y_2 = np.zeros_like(T_2)
    
    
    #set inital velocity and launch height values
    V_x2[0] = V_x0
    y_2[0] = height
    V_y2[0] = 0
    V_2[0] = V_x2[0]
  
  # update arrays with calculated values for acceleration (since drag force is devided by mass), 
  #velocities and positions in both x & y directions with conditional statement so that it stops at the ground level
  # using eulers stepping method
    for t in range(0,(n_steps-1)):
      
      #calculate next acceleration, velocities, and position if projectile is above the ground
      if y_2[t] >= 0 :
        
        a_dx2[t+1] = B_2*(V_2[t]*V_x2[t]) 
        a_dy2[t+1] = B_2*(V_2[t]*V_y2[t])
        
        V_x2[t+1] = V_x2[t] - (a_dx2[t])*dt
        V_y2[t+1] = V_y2[t] - (g + a_dy2[t])*dt 
        V_2[t+1] = np.sqrt((V_x2[t+1])**2 + (V_y2[t+1])**2)
        
        x_2[t+1] = x_2[t] + V_x2[t]*dt
        y_2[t+1] = y_2[t] + V_y2[t]*dt 
        
      else:
        break
        
    return V_2[:t+1], V_x2[:t+1], V_y2[:t+1], T_2[:t+1], x_2[:t+1], y_2[:t+1]
  
