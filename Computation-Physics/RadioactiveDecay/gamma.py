# Parent daughter population 

# ---- gamma > 1 -------

plotAnalyticNa, = plt.plot(T, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
plotNumericalNa, = plt.plot(T, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')

plotAnalyticNb1, = plt.plot(T, NB1_analytic, linewidth=10, color = 'purple', label = 'Analytic N$_B$')
plotNumericalNb1, = plt.plot(T, NB1_numeric, linewidth = 4, color = 'm', label = 'Numerical N$_B$')

xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa, plotAnalyticNb1, plotNumericalNb1], loc='best')
plt.savefig('HW1_NANB_plot1.pdf', bbox_inches='tight')

ratio1 = NB1_numeric/NA_numeric
ratio2 = NB2_numeric/NA_numeric
ratio3 = NB3_numeric/NA_numeric

analytic_ratio1 = NB1_analytic/NA_analytic
analytic_ratio2 = NB2_analytic/NA_analytic
analytic_ratio3 = NB3_analytic/NA_analytic


plotratio1, = plt.plot(T, ratio1, linewidth=4, color = 'b', label = 'Ratio N$_B$/N$_A$')


#graph stuff
xlabel = plt.xlabel(r'time') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$')
#plt.legend(handles=[ plotratio1], loc='best')
plt.savefig('HW1_ratio_plot1.pdf', bbox_inches='tight')




# ---- gamma = 1 -------

plotAnalyticNa, = plt.plot(T, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
plotNumericalNa, = plt.plot(T, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')

plotAnalyticNb2, = plt.plot(T, NB2_analytic, linewidth=10, color = 'purple', label = 'Analytic N$_B$')
plotNumericalNb2, = plt.plot(T, NB2_numeric, linewidth = 4, color = 'm', label = 'Numerical N$_B$')

xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa, plotAnalyticNb2, plotNumericalNb2], loc='best')
plt.savefig('HW1_NANB_plot2.pdf', bbox_inches='tight')

Dplotratio2, = plt.plot(T, ratio2, linewidth=4, color = 'b', label = 'Ratio N$_B$/N$_A$')


#graph stuff
xlabel = plt.xlabel(r'time') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$')
#plt.legend(handles=[ plotratio2], loc='best')
plt.savefig('HW1_ratio_plot2.pdf', bbox_inches='tight')




# ---- gamma < 1 -------

plotAnalyticNa, = plt.plot(T, NA_analytic, linewidth=10, color = 'b', label = 'Analytic N$_A$')
plotNumericalNa, = plt.plot(T, NA_numeric, linewidth = 4, color = 'cyan', label = 'Numerical N$_A$')

plotAnalyticNb3, = plt.plot(T, NB3_analytic, linewidth=10, color = 'purple', label = 'Analytic N$_B$')
plotNumericalNb3, = plt.plot(T, NB3_numeric, linewidth = 4, color = 'm', label = 'Numerical N$_B$')

xlabel = plt.xlabel(r'time ($\tau_{A}$)') 
ylabel = plt.ylabel('N')
plt.legend(handles=[plotAnalyticNa, plotNumericalNa, plotAnalyticNb3, plotNumericalNb3], loc='best')
plt.savefig('HW1_NANB_plot2.pdf', bbox_inches='tight')

plotratio3, = plt.plot(T, ratio3, linewidth=4, color = 'b', label = 'Ratio N$_B$/N$_A$')


#graph stuff
xlabel = plt.xlabel(r'time') 
ylabel = plt.ylabel('N$_{B}$/N$_{A}$')
#plt.legend(handles=[ plotratio3], loc='best')
plt.savefig('HW1_ratio_plot3.pdf', bbox_inches='tight')

