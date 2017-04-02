# -*- coding: utf-8 -*-
"""
Spyder Editor

@author:Qinhui Xu
GWID:G36978983
"""

import pandas as pd
import time
import matplotlib.pyplot as plt

def getData():
    """Reads multiple files and returns contents in a panda dataframe"""
    """Args: none"""
    """Returns: A list of contents"""
    start_time = time.time()
    """Create empty dataframe"""
    dfAll=pd.DataFrame({'Name' : [],'Sex' : [],'Count' : [],'Year' : []})
    print('Started ...')
    """Get the path of the file"""
    filelocation = input("Please provide the path of the file")
    for year in range(1880,2016):
        filename = 'yob'+str(year)+'.txt'
        filepath = filelocation + filename
        """Read the file into the dataframe"""
        df = pd.read_csv(filepath, header=None)
        df.columns = ['Name', 'Sex', 'Count']
        df['Year'] = str(year)
        """To concatenate the data"""
        dfAll = pd.concat([dfAll,df])     
    print('Done...')
    print ('It took', round(time.time()-start_time,4), 'seconds to read all the data into a dataframe.')
    return dfAll
    
def q1(myDF):
    """Compute the total number of births for each year and provide a formatted printout of that"""
    """Args: File"""
    """Returns: Nothing"""
    
    """dfCount is panda series"""
    dfCount = myDF['Count'].groupby(myDF['Year']).sum()
    s = '{:>5}'.format('Year')
    s = s + '{:>10}'.format('Births')
    print(s)
    """Make a format to print the data"""
    for myIndex, myValue in dfCount.iteritems():
        s = '{:>5}'.format(myIndex)
        s = s + '{:>10}'.format(str(int(myValue)))
        print (s)

        
def q2(myDF):
    """Compute the total births each year (from 1990 to 2014, inclusive of both) for males and females and provide a plot for that."""
    """Args: File"""
    """Returns:Nothing"""
    
    """Separate the data from 1990 t0 2014"""
    dfSubset = myDF[ (myDF['Year'] >= '1990') & (myDF['Year'] <= '2014') ]
    """Calculate the sum of the name with different sex each year"""
    dfCountBySex = dfSubset.groupby(['Year','Sex']).sum()
    """Draw the plot"""
    dfCountBySex.plot.bar(figsize=(10,10))  
    
def q3(myDF):
    """Print the top 5 names for each year starting in 1950"""
    """Args: File"""
    """Returns: Nothing"""
    s = ''
    s = '{:>5}'.format('Year')
    s = s + '{:>10}'.format('Name 1')
    s = s + '{:>10}'.format('Name 2')
    s = s + '{:>10}'.format('Name 3')
    s = s + '{:>10}'.format('Name 4')
    s = s + '{:>10}'.format('Name 5')
    print (s)
    """Go through all the years"""
    for i in range(1950,2016):
        """ Create a data frame for a matching year"""
        fn = myDF[(myDF['Year'] == str(i))]          
        """ Sort by count and retain the top five rows"""        
        fn = fn.sort_values('Count', ascending=False).head(5)   
        s = ''
        s = s = s + '{:>5}'.format(str(i))
        """ Now iterate through the data frame with five records"""
        for idx, row in fn.iterrows():
            s = s + '{:>10}'.format(row["Name"])
        print(s)

def q4(myDF):
    """Find the top 3 female and top 3 male names for years 2010 and up and and plot the frequency by gender."""
    """Args: File"""
    """Returns: Nothing"""
    
    """Make the foramt for display"""
    s = ''
    s = '{:>5}'.format('Year')
    s = s + '{:>10}'.format('Female 1')
    s = s + '{:>10}'.format('Female 2')
    s = s + '{:>10}'.format('Female 3')
    s = s + '{:>10}'.format('Male 1')
    s = s + '{:>10}'.format('Male 2')
    s = s + '{:>10}'.format('Male 3')
    print (s)
    """Create a dataframe for concatenate the data"""
    datagraph1=pd.DataFrame({'Count' : [],'Name' : [],'Sex' : [],'Year':[]})
    datagraph2=pd.DataFrame({'Count' : [],'Name' : [],'Sex' : [],'Year':[]})
    """Go through all the years of interests"""
    for i in range(2010,2016):
        """Subset the data by year and sex"""
        Ffemale = myDF[(myDF['Year'] == str(i)) & (myDF['Sex'] == 'F') ]  
        Fmale = myDF[(myDF['Year'] == str(i)) & (myDF['Sex'] == 'M') ]
        """Sort the data based on the count and remain the top3 names"""
        fn = Ffemale.sort_values('Count', ascending=False).head(3)
        fn2 = Fmale.sort_values('Count', ascending=False).head(3)
        """Concatenate the data"""
        datagraph1=pd.concat([datagraph1,fn])
        datagraph2=pd.concat([datagraph1,fn2])
        s = ''
        s = s + '{:>5}'.format(str(i))
        for idx, row in fn.iterrows():
            s = s + '{:>10}'.format(row["Name"])
        for idx, row in fn2.iterrows():
            s = s + '{:>10}'.format(row["Name"])
        print(s)
    dfCountBySex1 = datagraph1['Count'].groupby(datagraph1['Name']).sum()
    dfCountBySex2 = datagraph2['Count'].groupby(datagraph2['Name']).sum()
    """Plot the data"""
    plt.figure(1)
    plt.xlabel('Female')
    plt.ylabel('Count')
    plt.title='Top Names For Female'
    dfCountBySex1.plot.bar(color="red")            
    plt.figure(2)
    plt.xlabel('Male')
    plt.ylabel('Count')
    plt.title='Top Names For Male'
    dfCountBySex2.plot.bar(color="blue")   

def q5(myDF):
    """Plot the trend of the names 'John', 'Harry', 'Mary' and 'Marilyn' over all of the years of the data set."""
    """Args: File"""
    """Returns: Nothing"""
    
    """Subset the data with name John"""
    John = myDF[(myDF['Name'] == 'John')]
    """Make the sum of name John by year"""
    John =  John['Count'].groupby(John['Year']).sum()
    """Plot John"""
    plt.subplot(4,1,1)
    plt.ylabel('John')
    John.plot(color="red")
    
    """Subset the data with name Harry"""
    Harry = myDF[(myDF['Name'] == 'Harry')]
    """Make the sum of name Harry by year"""
    Harry =  Harry['Count'].groupby(Harry['Year']).sum()
    """Plot Harry"""
    plt.subplot(4,1,2)
    plt.ylabel('Harry')
    Harry.plot(color="blue")
    
    """Subset the data with name Mary"""
    Mary = myDF[(myDF['Name'] == 'Mary')]
    """Make the sum of name Mary by year"""
    Mary = Mary['Count'].groupby(Mary['Year']).sum()
    """Plot Mary"""
    plt.subplot(4,1,3)
    plt.ylabel('Mary')
    Mary.plot(color="green")
    
    """Subset the data with name Marilyn"""
    Marilyn = myDF[(myDF['Name'] == 'Marilyn')]
    """Make the sum of name Marilyn by year"""
    Marilyn = Marilyn['Count'].groupby(Marilyn['Year']).sum()
    """Plot Marilyn"""
    plt.subplot(4,1,4)
    plt.ylabel('Marilyn')
    Marilyn.plot(color="black")

    """Plotting 4 plots in one graph"""
    plt.figure(2)
    plt.xlabel('Years')
    plt.ylabel('Names')
    plt.xlim(1880,2015)
    John.plot(color="red",label='John')
    Harry.plot(color="blue",label='Harry')
    Mary.plot(color="green",label='Mary')
    Marilyn.plot(color="black",label='Marilyn')
    plt.legend()
    
def q6(myDF):
    """Find the ten names that have shown the greatest variation over the years. And plot this"""
    """Args: File"""
    """Rrturns: Nothing""" 
    """Subset the data by year and name, and make the sum fot the name"""
    dsYearCounts = myDF.groupby(['Year','Name']).sum()['Count']
    """To make a new dataframe"""
    data={}
    """Go through all the years for interests"""
    for year in range(1880,2016):
        data[str(year)]=dsYearCounts[str(year)]
    """To replace the NAA with 0, in order to calculate variations"""
    DataName = pd.DataFrame(data).fillna(0)
    """Transpose the DataName in order to use var function"""
    DataName = DataName.transpose()
    """Sort the variations"""
    dfNV = DataName.var().sort_values(ascending=False)
    """Retain the top10 names"""
    dfNV = dfNV.head(10)
    print(dfNV)
    plt.figure(1)
    plt.title='Top 10 names with highest Variation'
    dfNV.plot()
    