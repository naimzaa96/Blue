# 
We are defining precision as the difference between the time assiciated with the upper bound error and the time associated with the lower bound error. This can be expressed as a function of time:

precision = np.array([0]) #defining array


def prec(ratio, time, precision):
  
  error = 0.005 
  
  for i in range(0, (len(T)-1)):
    up = ratio[i]*(1+error)
    dn = ratio[i]*(1-error)
    if up < max(ratio):
      diff = np.interp(up, ratio, time) - np.interp(dn, ratio, time)
    
      precision = np.append(precision, diff)
    else:
      precision = np.append(precision, None)
    #print(i)
    
  return precision
  
  ratio1_precision = prec(ratio1, T, precision)
#
ratio2_precision = prec(ratio2, T, precision)

ratio3_precision = prec(ratio3, T, precision)

#len(ratio3_precision)

precisionplot1, = plt.plot(T, ratio1_precision, color = 'b', label = 'Precision ')
ratioplot1, = plt.plot(T, ratio1, color = 'r', label = 'Ratio ($\gamma > 1$)')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$ (red), Uncertainty (Units of $\tau_{A}$) (blue)')
plt.legend(handles=[precisionplot1, ratioplot1], loc='best')
plt.savefig('HW1_prec1.pdf', bbox_inches='tight')


precisionplot2, = plt.plot(T, ratio2_precision, color = 'b', label = 'Precision ')
ratioplot2, = plt.plot(T, ratio2, color = 'r', label = 'Ratio ($\gamma = 1$)')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$ (red), $t_{+} - t_{-}$ (blue)')
plt.legend(handles=[precisionplot2, ratioplot2], loc='best')
plt.savefig('HW1_prec2.pdf', bbox_inches='tight')


precisionplot3, = plt.semilogy(T, ratio3_precision, color = 'b', label = 'Precision ')
ratioplot3, = plt.semilogy(T, ratio3, color = 'r', label = 'Ratio ($\gamma < 1$)')


#graph stuff
xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$ (red), $t_{+} - t_{-}$ (blue)')
plt.legend(handles=[precisionplot3, ratioplot3], loc='best')
plt.savefig('HW1_prec3.pdf', bbox_inches='tight')





# Make an example plot with two subplots...
fig = plt.figure()
ax1 = fig.add_subplot(3,1,1)
precisionplot1, = plt.semilogy(T, ratio1_precision, color = 'b', label = 'Precision ')
ratioplot1, = plt.semilogy(T, ratio1, color = 'r', label = 'Ratio ($\gamma > 1$)')
plt.setp(ax1.get_xticklabels(), visible=False)

ax2 = fig.add_subplot(3,1,2)
precisionplot2, = plt.semilogy(T, ratio2_precision, color = 'b', label = 'Precision ')
ratioplot2, = plt.semilogy(T, ratio2, color = 'r', label = 'Ratio ($\gamma = 1$)')
# make these tick labels invisible
plt.setp(ax2.get_xticklabels(), visible=False)

plt.ylabel('$N_{B}/N_{A}$ (red) [$N_{A}(0)$] , $t_{uncertainty}$ (blue) [τ$_{A}$)]')

ax3 = fig.add_subplot(3,1,3)
precisionplot3, = plt.semilogy(T, ratio3_precision, color = 'b', label = 'Precision ')
ratioplot3, = plt.semilogy(T, ratio3, color = 'r', label = 'Ratio ($\gamma < 1$)')
plt.xlim(-.1, 100.0)
plt.ylim(0.00001 , 1E49)
plt.xlabel('time (in units of τ$_{A}$)')

plt.show()
fig.savefig('HW1_prec.pdf', bbox_inches='tight')


#xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
#ylabel = plt.ylabel('N$_{B}$/N$_{A}$ (Units of $N_{A}(0)$) (red), t_{error} (Units of $\tau_{A}$) (blue)')
#plt.legend(handles=[precisionplot3, ratioplot3], loc='best')
#plt.savefig('HW1_prec.pdf', bbox_inches='tight')
