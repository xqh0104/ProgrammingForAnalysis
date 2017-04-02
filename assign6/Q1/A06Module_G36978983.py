# -*- coding: utf-8 -*-
"""
Created on Thu Nov  17 18:12:27 2016

@author: xqh
"""

def readLPData(fn):
    """
    input = json file
    output = data in json file
    """
    import json
    
    try:
        with open(fn,'r') as f:
            LPdata = json.load(f)
        return LPdata
    except:
        return None
        
#a = readLPData("introLP.json")      

def createAndSolveLP(LPdata):
    """
    input = data in json file
    output = a dictionary including optimal value and decision variables
    """
    import pulp as plp
    
    if LPdata["objective"]=="MIN":
        my_model = plp.LpProblem("My Model", plp.LpMinimize)          
    elif LPdata["objective"]=="MAX":
        my_model = plp.LpProblem("My Model", plp.LpMaximize) 
    else:
        print ("Neither max or min")
        exit(0)
        
    
    decVars = LPdata["variables"] 
    #print (decVars)
    #input("Enter to continue...")
    
    x = plp.LpVariable.dict('%s', decVars, lowBound = 0) 
    
    objCoeffList = LPdata["objCoeffs"]   
    objective = dict(zip(decVars, objCoeffList))
    
    my_model += sum([objective[i]*x[i] for i in decVars])
    
    constraintKeys = LPdata["LHS"].keys()
    
    for key in constraintKeys:
        LHScoeffs = dict(zip(decVars,LPdata["LHS"][key]))
        
        if LPdata["conditions"][key] == '<=':
            my_model +=  sum([LHScoeffs[j]*x[j] for j in decVars]) <= LPdata["RHS"][key]
        elif LPdata["conditions"][key] == '>=':
            my_model +=  sum([LHScoeffs[j]*x[j] for j in decVars]) >= LPdata["RHS"][key]   
        elif LPdata["conditions"][key] == '==':
            my_model +=  sum([LHScoeffs[j]*x[j] for j in decVars]) == LPdata["RHS"][key]                      
        else:
            print ("Problems with constraint {} ".format(key))
            exit(0)
    
    
    # solve LP ===========================================================================
    lpDict = {}
    myProblem = my_model
    myProblem.writeLP("Shader.lp")
    #myProblem.solve(plp.GLPK())      
    myProblem.solve()
    """
    print ("Status:", plp.LpStatus[myProblem.status])
    
    for v in myProblem.variables():
        print (v.name, "=", v.varValue)
    print ("objective =", plp.value(myProblem.objective))
    print ("\nSensitivity Analysis\nConstraint\t\tShadow Price\tSlack")
    for name, c in myProblem.constraints.items():
        print (name, ":", c, "\t", c.pi, "\t\t", c.slack)
    """
    
    lpDict["Objective Function"] = plp.value(myProblem.objective)   
    #lpDict["Objective Function: "+str(objFunction)] = plp.value(myProblem.objective)
    d = {}
    for v in myProblem.variables():
        d.update({v.name:v.varValue})
    lpDict["Variables"] = d       
    
    return (lpDict)
         

def writeFile(filename,jsondata,myData): 
    """
    input = three parameters: filename of output txt, data in json file and the solution of problems
    output = None
    """
    
    try:
        with open(filename,"w") as f:
         #   f.write()
            
            verb = "The "+ jsondata['objective']+ " value is {:.3f}\n".format(myData["Objective Function"])
            #verb = "The minimum value is {:.3f}\n".format(myData["Objective Function"])
            for i in myData["Variables"]:
                verb += i+": " + "{:.3f}".format(myData["Variables"][i]) +"\n"
            f.write(verb)
            #print (verb)
            print ("Output being sent to " + filename)
            print ("Output written to" + filename)

    except:
        print ("Write operation was unsuccessful")        
    
    


    
    
    

         
            