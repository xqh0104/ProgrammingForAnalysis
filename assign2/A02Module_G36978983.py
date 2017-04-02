# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:05:59 2016

@author: Qinhui
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from sklearn import linear_model
from pandas import DataFrame
from sklearn.metrics import r2_score
from mpl_toolkits.mplot3d import *

#fileName=input("Please input your filename")

def fileInput(fileName):
    """
    Input = name of the input file
    output = numpy arrat
    """
    #arr = pd.read_csv(fileName)
    file = np.genfromtxt(fileName, delimiter=',')   
    arr = DataFrame(data = file, columns=['y','x1','x2'])
    arr = arr.as_matrix()
    return arr
    
def regress(myData):
    """
    Input = numpy array
    Column 1 in the array is the dependent variable
    Column 2 and 3 in the array are the independent variables
    Return = a list of coefficients
    """
    xarr = myData[:,1:]
    X = np.array([np.concatenate((v,[1])) for v in xarr])
    model = linear_model.LinearRegression(fit_intercept = True)
    yarr = myData[:,0]
    fit = model.fit(X,yarr)
    pred = model.predict(X)
    List=[fit.intercept_,fit.coef_[0],fit.coef_[1],r2_score(yarr,pred)]
    return(List)
    """
    print("Intercept : ",fit.intercept_)
    print("Slope : ", fit.coef_)
    pred = model.predict(X)
    r2 = r2_score(yarr,pred) 
    print ('R-squared: %.4f' % (r2))
    """
def myPlot(myData, b):
    """
    Input = numpy array with three columns
            Column 1 is the dependent variable
            Columns 2 and 3 are the independent variables
            and
            a column vector with the b coefficients
    Returns = Noting
    Output = 3D plot of the actual data and 
             the surface plot of the linear model
    """  
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib import cm      
    fig = plt.figure()
    ax = fig.gca(projection='3d')               # to work in 3d
    plt.hold(True)
    
    x_max = max(myData[:,1])    
    y_max = max(myData[:,2])   
    
    b0 = float(b[0])
    b1 = float(b[1])
    b2 = float(b[2])   
    
    x_surf=np.linspace(0, x_max, 100)                # generate a mesh
    y_surf=np.linspace(0, y_max, 100)
    x_surf, y_surf = np.meshgrid(x_surf, y_surf)
    z_surf = b0 + b1*x_surf +b2*y_surf         # ex. function, which depends on x and y
    ax.plot_surface(x_surf, y_surf, z_surf, cmap=cm.hot, alpha=0.2);    # plot a 3d surface plot
    
    x=myData[:,1]
    y=myData[:,2]
    z=myData[:,0]
    ax.scatter(x, y, z);                        # plot a 3d scatter plot
    
    ax.set_xlabel('x1')
    ax.set_ylabel('y2')
    ax.set_zlabel('y')

    plt.show()
    
    
    