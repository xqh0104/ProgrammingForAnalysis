# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:35:38 2016

@author: Qinhui
"""

import A02Module_G36978983 as md
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-b", "--brief", help="output the coefficients", action="store_true")
parser.add_argument("-v", "--verbose", help="description of equation", action="store_true")
parser.add_argument("-p", "--plot", help="plot the figure", action="store_true")
#parser.add_argument('-o', "--output", help="output the file", action="store_true")
parser.add_argument('-o', dest='outfile', action='store', help='output file')
parser.add_argument("fileName", type=str, help="input filename")
#parser.add_argument("outfile", type=str, help="output filename", default="output.txt")

args = parser.parse_args()


if args.brief: 
    MyData=md.fileInput(args.fileName)
    List=md.regress(MyData)
    print("Intercept:",List[0],"\n")
    print("b1:",List[1],"\n")
    print("b2:",List[2],"\n")
    
if args.verbose:
    MyData=md.fileInput(args.fileName)
    List=md.regress(MyData)
    print("The Equation is:\n")
    print("y= %.4f + %.4fX1 +%.4fX2\n"%(List[0],List[1],List[2]))
    print("The R-square value is\n ",List[3])
    print("The formatted input data is shown below:\n")
    print("   y    x1   x2")
    print("===================")
    print(MyData)

if args.plot: 
    MyData=md.fileInput(args.fileName)
    List=md.regress(MyData)
    md.myPlot(MyData,List)

if args.outfile:
    MyData=md.fileInput(args.fileName)
    List=md.regress(MyData)
    print("Intercept:",List[0],"\n")
    print("b1:",List[1],"\n")
    print("b2:",List[2],"\n")
    print("The R-square value is\n ",List[3])
    print("The result being sent to",args.outfile)
    with open(args.outfile, 'a') as f:
        f.write("Intercept:"+str(List[0])+"\n") 
        f.write("b1:"+str(List[1])+"\n")
        f.write("b2:"+str(List[2])+"\n")
        f.write("The R-square is:"+str(List[3])+"\n")
    
else:
    MyData=md.fileInput(args.fileName)
    List=md.regress(MyData)
    print("Intercept:",List[0],"\n")
    print("b1:",List[1],"\n")
    print("b2:",List[2],"\n")
    print("The R-square value is",List[3])
    
    
    