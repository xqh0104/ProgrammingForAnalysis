# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
@author = Xqh
"""
import os
import json
import pymongo

def getFileNames():
    """
    Input = name of JSON file
    Returns = JSON object
    """
    import os
    included_extensions = ['json'];
    file_names = [fn for fn in os.listdir(os.getcwd())
                  if any ([fn.endswith(ext)
                          for ext in included_extensions])];
    return file_names

#file_names = getFileNames()

def readAndStore(file_names):
    """
    input = json object
    output = the content writtent into the DATABASE
    """
    import json
    import pymongo
    # Start a mongodb client on the local machine using port 27017
    client = pymongo.MongoClient('localhost:27017')
    db = client['myDB']
    collection = db['A06']
    if (collection.count() != 0):
        collection.drop()
    collection = db['A06']
    length = len(file_names)
    #print(length)
    for i in range(0,length):
        #print(i)
        with open('/home/xqh/Documents/Programming/Assignment06/'+file_names[i], 'r') as f:
            jsonfile = json.load(f)
        db.A06.insert_one(jsonfile)
    
    allObjs = db.A06.find()
    #print (allObjs.count())
    return allObjs

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
    
    x = plp.LpVariable.dict('x_%s', decVars, lowBound = 0) 
    
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
    myProblem.solve()
    #myProblem.solve(plp.GLPK())      
    
    lpDict["Objective Function"] = plp.value(myProblem.objective)   
    #lpDict["Objective Function: "+str(objFunction)] = plp.value(myProblem.objective)
    d = {}
    for v in myProblem.variables():
        d.update({v.name:v.varValue})
    lpDict["Variables"] = d       
    #print(lpDict)
    return (lpDict)
    
#allObjs = readAndStore(file_names)
#results = []
#for x in allObjs:
#    optimal = createAndSolveLP(x)
#    print("The optimal value is ",optimal['Objective Function'])
"""
def outputDatabase(allObjs):
    client = pymongo.MongoClient('localhost:27017')
    db = client['myDB']
    collection = db['LP']
    if (collection.count() != 0):
        collection.drop()
    collection = db['LP']
    for x in allObjs:
        optimal = createAndSolveLP(x)
        db.LP.insert(
        {
            'ProblemName' : x['name'],
            'OptimalValue' : optimal['Objective Function']
            
        })
    Objs = db.LP.find()

    for x in Objs:
        print(x)
"""

def outputToDatabase(allObjs,tableName):
    """
    input: the solution of LP and tableName
    output： None
    """
    import pymysql as myDB
    conn = myDB.connect('localhost','root','root')
    cursor = conn.cursor()
    
    sql = 'SHOW DATABASES;'
    cursor.execute(sql)
    
    sql = 'DROP DATABASE IF EXISTS LP;'
    cursor.execute(sql)
    
    sql = 'CREATE DATABASE LP;'
    cursor.execute(sql)
    
    sql = ' USE LP; ' 
    cursor.execute(sql)
    
    sql = '''
            DROP TABLE IF EXISTS %s;
            CREATE TABLE %s(
            ProblemName CHAR(20),
            OptimalValue CHAR(20));
            '''%(tableName,tableName)
    cursor.execute(sql)
    
    for x in allObjs:
        optimal = createAndSolveLP(x)
        #print(x)
        #print(optimal)
        problem_Name = x['name']
        opt_Val = optimal['Objective Function']
        #print(problem_Name)
        #print(opt_Val)
        sql = '''
                INSERT INTO %s (ProblemName,OptimalValue) VALUES ("%s",%.3f);
                '''%(tableName,problem_Name,opt_Val)
        cursor.execute(sql)
        conn.commit()

    cursor.close()
    
def outputToTXT(allObjs,textFile):
    """
    input = the solution of LP and textFile name
    output = None
    """
    for x in allObjs:
        optimal = createAndSolveLP(x)
        with open(textFile, 'a') as f:
            f.write("The problem name is "+x['name']+"\n")
            f.write("The optimal value is %.3f "%optimal['Objective Function']+"\n")
