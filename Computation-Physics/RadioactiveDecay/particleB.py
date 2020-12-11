# in terms of tau
# tau_A's CANNOT BE SMALLER THAN dt or we will get alternating values of the population of partical NB
tau_B1  =2/3 #tau_B smaller than tau_A
tau_B2  = 1 #tau_B equal to tau_A
tau_B3  = 100 #tau_B greater than tau_A
NB0 = 0

NB1 = np.array([NB0]) #Defining an array.
NB2 = np.array([NB0])
NB3 = np.array([NB0])

# for loop that will be at t=0 and move to t=10 tau_A by taking steps for 0.001 tau_A.
# the loop will record the a new NA value and append that value to the array. 
# Next it will make a recording given the previous measurement and append again. 
# and so on until t=10 tau_A is met. 

def functionB(NB1, NB2, NB3, tau_B1, tau_B2, tau_B3, NA, tau_A,   dt):
  
  n_steps = math.ceil(time/dt) #this gives the number of steps overall. If not in function would be a constant.
  
  T = np.linspace(0,time, n_steps)#gives us all (10000 for dt) time values that correspong to the NA values with a maximum time of t=1000. 
  
  
  for t in range(0,n_steps-1):
    # function for array where tau_B is smaller than tau_A
    newNB1 = NB1[t]*(1-(dt/tau_B1)) + (NA[t]/tau_A)*dt
    NB1 = np.append(NB1, newNB1)
   
    
    # function for array where tau_B is equal to tau_A
    newNB2 = NB2[t]*(1-(dt/tau_B2)) + (NA[t]/tau_A)*dt
    NB2 = np.append(NB2, newNB2)
    
    
    # function for array where tau_B is greater than tau_A
    newNB3 = NB3[t]*(1-(dt/tau_B3)) + (NA[t]/tau_A)*dt
    NB3 = np.append(NB3, newNB3)
    
    
    newNA = NA[t] - (NA[t]/tau_A)*dt
    NA = np.append(NA,newNA)
    #print(newNB, NB[t])
  return NB1, NB2, NB3, T

#the function is not necessary, but it is useful later when checking the error. 
NB1_numeric,NB2_numeric, NB3_numeric, T = functionB(NB1, NB2, NB3, tau_B1, tau_B2, tau_B3, NA, tau_A,   dt) 

# Where tau_a>tau_b
plotAnalyticNb1, = plt.plot(T, NB1_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
plotNumericalNb1, = plt.plot(T, NB1_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[plotAnalyticNb1, plotNumericalNb1], loc='best')
plt.savefig('HW1_NB1_plot1.pdf', bbox_inches='tight')

# Plot in semilog to later compare how data changes with increased time steps:

splotAnalyticNb1, = plt.semilogy(T, NB1_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
splotNumericalNb1, = plt.semilogy(T, NB1_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[splotAnalyticNb1, splotNumericalNb1], loc='best')
plt.savefig('HW1_NB1_plot2.pdf', bbox_inches='tight')

plotAnalyticNb2, = plt.plot(T, NB2_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
plotNumericalNb2, = plt.plot(T, NB2_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[plotAnalyticNb2, plotNumericalNb2], loc='best')
plt.savefig('HW1_NB2_plot1.pdf', bbox_inches='tight')

splotAnalyticNb2, = plt.semilogy(T, NB2_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
splotNumericalNb2, = plt.semilogy(T, NB2_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[splotAnalyticNb2, splotNumericalNb2], loc='best')
plt.savefig('HW1_NB2_plot2.pdf', bbox_inches='tight')

plotAnalyticNb3, = plt.plot(T, NB3_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
plotNumericalNb3, = plt.plot(T, NB3_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[plotAnalyticNb3, plotNumericalNb3], loc='best')
plt.savefig('HW1_NB3_plot1.pdf', bbox_inches='tight')

splotAnalyticNb3, = plt.semilogy(T, NB3_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
splotNumericalNb3, = plt.semilogy(T, NB3_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[splotAnalyticNb3, splotNumericalNb3], loc='best')
plt.savefig('HW1_NB3_plot2.pdf', bbox_inches='tight')

# Measuring numerical accuracy

NB1_10, NB2_10, NB3_10, T10 = functionB(NB1, NB2, NB3, tau_B1, tau_B2, tau_B3, NA, tau_A,  10*dt) 
NB1_100, NB2_100, NB3_100, T100 = functionB(NB1, NB2, NB3, tau_B1, tau_B2, tau_B3, NA, tau_A,  dt*100)



plotAnalyticNb1, = plt.semilogy(T/tau_A, NB1_analytic, linewidth=10, color = 'b', label = 'Analytic N$_B$')
plotNumericalNb1, = plt.semilogy(T/tau_A, NB1_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_B$')
plotNumericalNb1_10, = plt.semilogy(T10/tau_A, NB1_10, linewidth = 4, color = 'r', label = 'Numerical N$_B$ w/ 10x timestep')
#plotNumericalNb1_100, = plt.semilogy(T100/tau_A, NB1_100, linewidth = 4, color = 'purple', label = 'Numerical N$_B$ w/ 100x timestep')

xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$')
plt.legend(handles=[plotAnalyticNb1, plotNumericalNb1, plotNumericalNb1_10], loc='best')
#plt.legend(handles=[plotAnalyticNb1, plotNumericalNb1, plotNumericalNb1_10, plotNumericalNb1_100], loc='best')
plt.savefig('HW1_NB1_plot3.pdf', bbox_inches='tight')
