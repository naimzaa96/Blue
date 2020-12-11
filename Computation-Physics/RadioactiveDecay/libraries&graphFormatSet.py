## Libraries

import numpy as np
import scipy as sp
from scipy.interpolate import interp1d
from IPython.display import display, Markdown, Latex
import pandas as pd
import math
from astropy.io import ascii
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.colorbar as cb
import ipywidgets
import glob

#Formatting our graphs

plt.style.use('seaborn')

%matplotlib inline
%config InlineBackend.figure_format = 'retina'
matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'
matplotlib.rc('xtick', labelsize=20) 
matplotlib.rc('ytick', labelsize=20)

plt.rcParams['figure.autolayout'] = False
plt.rcParams['axes.labelsize'] = 20
plt.rcParams['axes.titlesize'] = 20
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2.0
plt.rcParams['lines.markersize'] = 8
plt.rcParams['legend.fontsize'] = 20
plt.rcParams['figure.figsize']=(10,10)

font = {'family' : 'serif',
        'weight' : 'normal',
        'size'   : '18'}

matplotlib.rc('font', **font)
