# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 15:43:37 2016

@author: xqh
"""


import argparse as ap
import sys
import A06Module_G36978983 as md


fileName = sys.argv[1]

myP = ap.ArgumentParser()

myGroup = myP.add_mutually_exclusive_group()                                          
myGroup.add_argument("-b","--brief", action = "store_true")                      
myGroup.add_argument("-d","--detail", action = "store_true")                           
myP.add_argument('-o', '--outfile', help='output file')
myP.add_argument('fileName', help="The file name of myData", type = str)

myArgs = myP.parse_args()

#jsonfile and solution
jsondata = md.readLPData(fileName) ######
myData = md.createAndSolveLP(md.readLPData(fileName))     

if myArgs.brief:                                                                   
    print(myData["Objective Function"])         

elif myArgs.detail:    
    print ("The "+ jsondata['objective']+ " value is {:.3f}".format(myData["Objective Function"]))                                                               
    #print ("The minimum value is {:.3f}".format(myData["Objective Function"]))
    print ("The decision variables and their values are:")
    for i in myData["Variables"]:
        print (i+": " + "{:.3f}".format(myData["Variables"][i]))   
   
else:   #default                                                                             
    print ('The optimal value is {:.3f}'.format(myData["Objective Function"]))                
    
if myArgs.outfile:
   md.writeFile(myArgs.outfile, jsondata, myData)



