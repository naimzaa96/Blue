# Because the analytic model is accurate, we divide the absolute value of the difference between the analytic model and the numberic model by the analytic model so that we get data as a percentage of the correct model.

physical_accuracy = np.array([])

def difference(analytic_ratio, ratio, physical_accuracy):
  
  for x in range(0, len(ratio-1)):
    
    subtract = 100*np.abs(analytic_ratio[x] - ratio[x])/analytic_ratio[x]
    
    physical_accuracy = np.append(physical_accuracy, subtract)
    
  return physical_accuracy
  
  
phys_NA1 = difference(analytic_ratio1, ratio1, physical_accuracy)
phys_NA2 = difference(analytic_ratio2, ratio2, physical_accuracy)
phys_NA3 = difference(analytic_ratio3, ratio3, physical_accuracy)


NA_PhysicalAccuracy1, = plt.plot(T, phys_NA1 , label = '$\gamma > 1$' )
NA_PhysicalAccuracy2, = plt.plot(T, phys_NA2 , label = '$\gamma = 1$' )
NA_PhysicalAccuracy3, = plt.plot(T, phys_NA3 , label = '$\gamma < 1$' )


xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('(units of $N_{A, analytic}$)')
plt.legend(handles=[NA_PhysicalAccuracy1, NA_PhysicalAccuracy2, NA_PhysicalAccuracy3], loc='best')
plt.savefig('HW1_ratio_PhysAcc1all.pdf', bbox_inches='tight')


