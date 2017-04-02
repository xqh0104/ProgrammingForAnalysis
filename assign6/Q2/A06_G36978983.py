# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author = Xqh
"""
import A06Module_G36978983 as md
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-t', dest='textFile', action='store', help='output file')
parser.add_argument('-d', dest='tableName', action='store', help='output file')

args = parser.parse_args()

# output sent to the textfile

file_names = md.getFileNames()
allObjs = md.readAndStore(file_names)
for x in allObjs:
    optimal = md.createAndSolveLP(x)
    print("The optimal value for", x['name'],"is %.3f"%optimal['Objective Function'])
    
if args.textFile:
    file_names = md.getFileNames()
    allObjs = md.readAndStore(file_names)
    print("Output being sent to file: ",args.textFile)
    md.outputToTXT(allObjs,args.textFile)
    print("Output written to file: ",args.textFile)
"""
    for x in allObjs:
        optimal = md.createAndSolveLP(x)
        print("The optimal value for", x['name'],"is",optimal['Objective Function'])
        """   
if args.tableName:
    file_names = md.getFileNames()
    allObjs = md.readAndStore(file_names)
    """
    for x in allObjs:
        optimal = md.createAndSolveLP(x)
        print("The optimal value for", x['name'],"is",optimal['Objective Function'])
        """
    print("Output being sent to table: ",args.tableName," in the LP database")
    md.outputToDatabase(allObjs,args.tableName)
    print("Output written to table: ",args.tableName," in the LP database")
     
"""          
else:
    file_names = md.getFileNames()
    allObjs = md.readAndStore(file_names)
    for x in allObjs:
        optimal = md.createAndSolveLP(x)
        print("The optimal value for", x['name'],"is",optimal['Objective Function'])
   
""" 
