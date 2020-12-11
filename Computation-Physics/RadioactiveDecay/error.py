#Define the error.

# # To do this so we can avoid the spaces between the points, I built a code that simply makes the indices within some range we are interested in read "True" while the indices outside this range reads "False". Then the indicese that read "True" are isolated so that the values of the ratio and the time for those indices can be made into arrays which can be plotted over the ratio and used to give the estimated time error.

point = 5000 #value of ratio to be used in finding the time error
error = 0.005

upper = ratio3 < (point + point*error) #boolian values for indices for the values of the indeces in ratio that are lower than (point + point*error)
lower = ratio3 > (point - point*error) #boolian values for indices for the values of the indeces in ratio that are greater than (point - point*error)
pop_error_range = np.logical_and(lower, upper) # produces boolian array where values are true between lower and upper and false elsewhere. 
ind = np.argwhere(pop_error_range == 1) #provides a list of the indices of "ratio" that gave True values
time_error_array = T[ind] #Gives the time values of those indicese
ratio_error_array = ratio3[ind] #Gives the ratio values of those indices

# To accurately define the error in time, we have to find the value of the difference between the maximum time in the error range and the time at the point:
# 𝑡+=𝑡𝑝𝑜𝑖𝑛𝑡+𝑝𝑜𝑖𝑛𝑡⋅𝑒𝑟𝑟𝑜𝑟−𝑡𝑝𝑜𝑖𝑛𝑡 
# and the difference between the time at the point and the minimum time in the error range:
# 𝑡−=𝑡𝑝𝑜𝑖𝑛𝑡−𝑡𝑝𝑜𝑖𝑛𝑡−𝑝𝑜𝑖𝑛𝑡⋅𝑒𝑟𝑟𝑜𝑟. 
# With these we can take the difference between  𝑡+  and  𝑡− . If the value is positive the time range from the point to the maximum time in the error range is greater which would make  𝑡+  the value of the error in time.

# To do so means we need the index for ratio[closest to point]. This next bit of code gives us the nearest index to the point value.

idx = (np.abs(ratio3-point)).argmin() # shifts all the values down (to the left on the number line) by the amount direction from the point.
                                      #the value cslosest to zero will now be the value that was closest to the point. 
                                      #Taking the absolute value makes that value the smallest value in the array. 
                                      #using np.argmin gives us the indices of that value. 
                                      
# error precision
t_upper = max(time_error_array)[0]
t_lower = min(time_error_array)[0]
t_point = T[idx]

t_upper - t_lower

# To determine the error in time we use
# (𝑡𝑢𝑝𝑝𝑒𝑟−𝑡𝑝𝑜𝑖𝑛𝑡)−(𝑡𝑝𝑜𝑖𝑛𝑡−𝑡𝑙𝑜𝑤𝑒𝑟) 
# If the result is positive the upper range becomes the time error. If negative the lower range becomes the error.

(t_upper - t_point) - (t_point - t_lower)

time_error_upper = max(time_error_array) - T[idx]
time_error_lower = T[idx] - min(time_error_array)
time_error_upper[0] , time_error_lower[0]


#Making 2 points to illustrate difference in error.

RATIO = ratio1

point_ill_1 =0.5
error_ill_1 = 0.1 #acuracy of measurement (this is set much higher to exaggerate the error range for figure - actual error is 0.005)

upper_ill_1 = RATIO < (point_ill_1 + point_ill_1*error_ill_1) #boolian values for indices for the values of the indeces in ratio that are lower than (point + point*error)
lower_ill_1 = RATIO > (point_ill_1 - point_ill_1*error_ill_1) #boolian values for indices for the values of the indeces in ratio that are greater than (point - point*error)

pop_error_range_ill_1 = np.logical_and(lower_ill_1, upper_ill_1) # produces boolian array where values are true between lower and upper and false elsewhere. 

ind_ill_1 = np.argwhere(pop_error_range_ill_1 == 1) #provides a list of the indices of "ratio" that gave True values

time_error_array_ill_1 = T[ind_ill_1] #Gives the time values of those indicese

ratio_error_array_ill_1 = RATIO[ind_ill_1] #Gives the ratio values of those indices







point_ill_2 = 1.5
error_ill_2 = 0.1 #acuracy of measurement (this is set much higher to exaggerate the error range for figure - actual error is 0.005)

upper_ill_2 = RATIO < (point_ill_2 + point_ill_2*error_ill_2) #boolian values for indices for the values of the indeces in ratio that are lower than (point + point*error)
lower_ill_2 = RATIO > (point_ill_2 - point_ill_2*error_ill_2) #boolian values for indices for the values of the indeces in ratio that are greater than (point - point*error)

pop_error_range_ill_2 = np.logical_and(lower_ill_2, upper_ill_2) # produces boolian array where values are true between lower and upper and false elsewhere. 

ind_ill_2 = np.argwhere(pop_error_range_ill_2 == 1) #provides a list of the indices of "ratio" that gave True values

time_error_array_ill_2 = T[ind_ill_2] #Gives the time values of those indicese

ratio_error_array_ill_2 = RATIO[ind_ill_2] #Gives the ratio values of those indices



idx_ill_1 = (np.abs(RATIO-point_ill_1)).argmin()
idx_ill_2 = (np.abs(RATIO-point_ill_2)).argmin()


t_upper_ill_1 = max(time_error_array_ill_1)[0]
t_lower_ill_1 = min(time_error_array_ill_1)[0]
t_point_ill_1 = T[idx_ill_1]


t_upper_ill_2 = max(time_error_array_ill_2)[0]
t_lower_ill_2 = min(time_error_array_ill_2)[0]
t_point_ill_2 = T[idx_ill_2]

plotratio, = plt.plot(T, RATIO, linewidth=4, color = 'b', label = 'Ratio N$_B$/N$_A$')
ploterror1, = plt.plot(time_error_array_ill_1, ratio_error_array_ill_1, linewidth=4, color = 'y', label = 'Error ')
ploterror2, = plt.plot(time_error_array_ill_2, ratio_error_array_ill_2, linewidth=4, color = 'y', label = 'Error ')



# Error for the second point
plt.plot([t_point_ill_2,t_point_ill_2],[0,point_ill_2], 'y--', linewidth = 2)
plt.plot([0,t_point_ill_2],[point_ill_2,point_ill_2], 'y--', linewidth = 2)

# Projections
upper_error_1 = plt.plot([t_lower_ill_2,t_lower_ill_2],[0,point_ill_2 - point_ill_2*error_ill_2], 'r--', linewidth = 2, label = 'Lower Error Projection')
plt.plot([0,t_lower_ill_2],[point_ill_2 - point_ill_2*error_ill_2,point_ill_2 - point_ill_2*error_ill_2], 'r--', linewidth = 2)

lower_error_1 = plt.plot([t_upper_ill_2,t_upper_ill_2],[0,point_ill_2 + point_ill_2*error_ill_2], 'g--', linewidth = 2 , label = 'Upper Error Projection')
plt.plot([0,t_upper_ill_2],[point_ill_2 + point_ill_2*error_ill_2,point_ill_2 + point_ill_2*error_ill_2], 'g--', linewidth = 2)


# Error for the first point
plt.plot([t_point_ill_1,t_point_ill_1],[0,point_ill_1], 'y--', linewidth = 2)
plt.plot([0,t_point_ill_1],[point_ill_1,point_ill_1], 'y--', linewidth = 2)

# Projections
plt.plot([t_lower_ill_1,t_lower_ill_1],[0,point_ill_1 - point_ill_1*error_ill_1], 'r--', linewidth = 2)
plt.plot([0,t_lower_ill_1],[point_ill_1 - point_ill_1*error_ill_1,point_ill_1 - point_ill_1*error_ill_1], 'r--', linewidth = 2)

plt.plot([t_upper_ill_1,t_upper_ill_1],[0,point_ill_1 + point_ill_1*error_ill_1], 'g--', linewidth = 2)
plt.plot([0,t_upper_ill_1],[point_ill_1 + point_ill_1*error_ill_1,point_ill_1 + point_ill_1*error_ill_1], 'g--', linewidth = 2)



xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$')
plt.legend(handles=[ plotratio, ploterror1], loc='best')
plt.savefig('HW1_error_plot1.pdf', bbox_inches='tight')


