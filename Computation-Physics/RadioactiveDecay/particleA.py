## Particle A
tau_A = 1 #time stuffs
NA0 = 1 #100% of particles  
dt = 0.01 #tau_A's -> These are the step (or time interval) sizes. [Why did we choose this?)
time = 100 #(tau_A's)  -> Overall time (span) for decay.

NA = np.array([NA0]) #Defining an array.


# for loop that will be at t=0 and move to t=10 tau_A by taking steps for 0.001 tau_A.
# the loop will record the new NA value and append that value to the array. 
# Next it will make a recording given the previous measurement and append again. 
# and so on until t=10 tau_A is met. 

def function(NA, tau_A,  dt):
  
  n_steps = math.ceil(time/dt) #this gives the number of steps overall. If not in function would be a constant.
  
  T = np.linspace(0,time, n_steps)#gives us all (10000 for dt) time values that correspong to the NA values with a maximum time of t=1000. 
  
  
  for t in range(0,n_steps-1):
    newNA = NA[t] - (NA[t]/tau_A)*dt
    NA = np.append(NA,newNA)
  return NA, T

#the function is not necessary, but it is useful later when checking the error. 

# Because of the function, we have to access the numeric results. If we were to remove the function NA would be the numeric result.
NA_numeric, T = function(NA, tau_A, dt)
NA_numeric

## Plotting Numeric vs Analytic
plotAnalyticNa, = plt.plot(T, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
plotNumericalNa, = plt.plot(T, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_A$)') 
ylabel = plt.ylabel('N$_{A}$')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa], loc='best')
plt.savefig('HW1_NA_plot1.pdf', bbox_inches='tight')

splotAnalyticNa, = plt.semilogy(T, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
splotNumericalNa, = plt.semilogy(T, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{A}$')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa], loc='best')
plt.savefig('HW1_NA_plot2.pdf', bbox_inches='tight')

# Meausuring accuracy
NA10, T10 = function(NA, tau_A, dt*10) 
NA100, T100 = function(NA, tau_A, dt*100)
NA500, T500 = function(NA, tau_A, dt*500)

plotAnalyticNa, = plt.semilogy(T/tau_A, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
plotNumericalNa, = plt.semilogy(T/tau_A, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')
plotNumericalNa10, = plt.semilogy(T10/tau_A, NA10, linewidth = 4, color = 'r', label = 'Numerical N$_A$ w/ 10x timestep')
# plotNumericalNa100, = plt.semilogy(T100/tau_A, NA100, linewidth = 4, color = 'purple', label = 'Numerical N$_A$ w/ 100x timestep')
# plotNumericalNa500, = plt.semilogy(T500/tau_A, NA500, linewidth = 4, color = 'm', label = 'Numerical N$_A$ w/ 500x timestep')

xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{A}$')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa, plotNumericalNa10, plotNumericalNa100, plotNumericalNa500], loc='best')
plt.savefig('HW1_NA_plot3.pdf', bbox_inches='tight')

