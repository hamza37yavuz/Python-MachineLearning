import numpy as np
import pandas as pd

# CREATING A NEW SERIES
# Creating a Series using a dictionary
name_age = {"Hamza" : 20, "Sinan" : 30, "Samet" : 40}
print(pd.Series(name_age))
# Creating a Series using a list
age = [20,30,40]
name = ["Hamza","Sinan","Samet"]
print(pd.Series(data = age,index = name))
# Creating a Series using a numpy array
array = np.array(age)
print(pd.Series(data = array))
print("\n")

# CREATING SERIES WITH DIFFERENT VALUES IN DIFFERENT WAYS
print(pd.Series(["A","B","C"],["Hamza","Ahmet","Cem"])) # both index and content are strings
grades = pd.Series([95,80,75],["Hamza","Ahmet","Cem"])
grades2 = pd.Series([75,90,65],["Hamza","Ahmet","Cem"])
print(grades+grades2)
print("\n")
# Accessing an element from a Series
print(grades2["Cem"])
print("\n")
# What happens if an index value exists on one side but not the other
grades = pd.Series([20,30,40,50],["a","b","c","d"])
grades2 = pd.Series([20,30,40,50],["a","f","g","c"])
print(grades+grades2)
print("\n")

# DATA FRAME PANDAS
print("-------------DATA FRAME PANDAS----------")
print("\n")
# INTRODUCTION
data = np.random.randn(4,3)
dataFrame = pd.DataFrame(data)
print(dataFrame)
print(type(dataFrame))
print("\n")

# ADDING NEW ROWS AND COLUMNS
newDataFrame = pd.DataFrame(data,index = ["Hamza","Samet","Umut","Hatice"], columns = ['Salary','Age','Working Hours'])
print(newDataFrame)
print(newDataFrame[['Salary','Age']]) # returns salary and age columns
print("\n")
# Getting a value from a data frame
print(newDataFrame.loc['Hamza'])
print("\n")
# Here a retirement column has been added
newDataFrame['Retirement'] = newDataFrame['Age'] + newDataFrame['Age']
print(newDataFrame)
print("\n")

# DROPPING A COLUMN OR ROW
print(newDataFrame.drop('Retirement',axis = 1)) # axis=1 compares across columns
print(newDataFrame.drop('Hamza',axis = 0)) # axis=0 compares across rows
print(newDataFrame) # the column we dropped came back, drop doesn't permanently delete this way
print("\n")
newDataFrame.drop('Retirement',axis = 1,inplace = True) # inplace=True deletes the column permanently
print(newDataFrame) # the same operation above can also be done for rows
print("\n")

# ACCESSING DATA WITH .loc FUNCTION
print(newDataFrame.loc['Hamza']['Working Hours'])
print(newDataFrame.loc['Hamza','Working Hours'])
print("\n")

# CONVERTING DATA FRAMES TO BOOLEAN VALUES
print(newDataFrame < 0)
print(newDataFrame[newDataFrame < 0])
print(newDataFrame[newDataFrame["Age"] > 0])
print("\n")

# CHANGING THE INDEX
print(newDataFrame.reset_index()) # use inplace=True if you want to make it permanent
print(newDataFrame)
new_index = ['Ham','Sam','Um','Hat']
newDataFrame['New Index'] = new_index
print(newDataFrame)
print(newDataFrame.set_index('New Index',inplace=True)) # use inplace=True if you want to make it permanent
print(newDataFrame.loc['Ham'])

# MULTI INDEX
index1 = ['primary','primary','middle','middle']
index2 = ['Hamza','Ahmet','Hasan','Samet']
multi = list(zip(index1,index2))
print(multi) # the two indices are now paired together
print(type(multi)) # let's check the type

# Preparing the zipped index1 and index2 in list structure for the Data Frame
multi = pd.MultiIndex.from_tuples(multi) 
print(multi)
print(type(multi)) # the type has changed
# creating other column data as a list then converting to an array
dataList = np.array([[2,282],[1,374],[3,211],[4,202]])
# now let's create the data frame
newDataFrame = pd.DataFrame(dataList,index = multi,columns=['Class','Number'])
print(newDataFrame)
# now let's see how to access data within this data frame
print(newDataFrame.loc['primary'])
print(newDataFrame.loc['middle'])
print("\n")
print(newDataFrame.loc['primary'].loc['Hamza'])
print("\n")
print(newDataFrame.loc['middle'].loc['Samet'])

# -- PANDAS OPERATIONS --
# Missing Data (data that needs to be deleted or filled)
# first let's create the data frames
weather = {"Istanbul":[30,29,np.nan],"Izmir":[40,39,38],"Ankara":[20,np.nan,25]}
weather = pd.DataFrame(weather)
weather2 = {"Istanbul":[30,29,np.nan],"Izmir":[40,39,38],"Ankara":[20,np.nan,25],"Antalya":[36,np.nan,np.nan]}
weather2 = pd.DataFrame(weather2)
print(weather)
print(weather2)
print("\n")
# now let's work with missing data

# removed all rows with missing data from the data (one-time)
print(weather.dropna()) 
# removed all columns with missing data (one-time)
print(weather.dropna(axis=1)) 
# removed columns that have more than 2 missing values from the data (one-time)
print(weather.dropna(axis=1, thresh=2)) 
# fills all empty places in the data one-time. use inplace=True for permanent change
print(weather.fillna(10))
print("\n") 

# GroupBy dataframe.groupby(name)
companyData = {"Department" : ["Software","Software","Marketing","Marketing","Legal","Legal"],
          "Employee Name" : ["Ahmet","Mehmet","Hamza","Samet","Emirhan","Hatice"],
          "Salary" : [1000,1500,2000,2500,3000,3500]
          }
companyData = pd.DataFrame(companyData)
print(companyData)
companyObj = companyData.groupby("Department")
print(companyObj) # this will output as an object
print("\n")
# using other functions with the object
# with this object we can do everything we could do in probability and statistics class
print(companyObj.describe()) # get all descriptions
print(companyObj.min()) # minimum value
print(companyObj.max()) # maximum value
# print(companyObj.mean()) # calculate the average
print(companyObj.count()) # number of data in each department
print("\n")
# Concat
# Merging different data frames with the Concat function
sports = {"Name" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Sport" : ["Running","Swimming","Running","Basketball"],
        "Calories" : [100,200,300,400]
        }
sports1 = {"Name" : ["Emirhan","Hatice","Fatih","Furkan"],
         "Sport" : ["Football","Badminton","Volleyball","Basketball"],
         "Calories" : [500,600,700,800]
         }
sports = pd.DataFrame(sports)
sports1 = pd.DataFrame(sports1)
# if we don't specify axis in concat, it defaults to axis=0. to merge columns, set axis=1
sports2 = pd.concat([sports,sports1],axis=0) # we can pass more than 2 data frames but here we passed two

# MERGE
mergeSports = {"Name" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Sport" : ["Running","Swimming","Running","Basketball"]
        }
mergeSports1 = {"Name" : ["Ahmet","Mehmet","Hamza","Samet"],
        "Calories" : [100,200,300,400]
        }
mergeSports = pd.DataFrame(mergeSports)
mergeSports1 = pd.DataFrame(mergeSports1)
# one data doesn't have calorie values and it's seen that name values are the same
# in this case we can merge, and after merging the calorie values are added to mergeSports
sportsData = pd.merge(mergeSports,mergeSports1,on="Name")
print(sportsData)
print("\n")
# Other Operations
print(companyData["Department"].unique()) # shows all the different departments
print(companyData["Department"].nunique()) # shows the number of departments
print(companyData["Department"].value_counts()) # shows how many people are in each department
print("\n")
def netSalary(salary):
        return salary * 0.66
print(companyData["Salary"].apply(netSalary)) # lets us apply a function we wrote earlier to the data
print(companyData["Department"].isnull()) # checks if there are null values in the data
print("\n")

# Pivot Table
cartoon = {"Character Class" : ["South Park","South Park","Simpson","Simpson","Simpson"],
           "Character Name" : ["Cartman","Kenny","Homer","Bart","Bart"],
           "Character Score" : [10,11,12,20,25]}
cartoon = pd.DataFrame(cartoon)
print(cartoon)
# with pivot_table, if there are two data entries for the same element, we can assign a single value using different functions
print(cartoon.pivot_table(values="Character Score",index=["Character Class","Character Name"],aggfunc=np.sum))
