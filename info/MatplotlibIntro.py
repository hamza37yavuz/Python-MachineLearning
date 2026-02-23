# MATPLOTLIB
import numpy as np
import matplotlib.pyplot as plt
# CREATING A GRAPH
age = [10,22,30,40,50,60,65,70,75,80]
weight = [30,70,80,85,90,92,95,100,90,85]
# convert to numpy array
age = np.array(age)
weight = np.array(weight)
# Let's look at the graph
plt.plot(age,weight,"r")
# Other operations on the graph
plt.xlabel("Age")
plt.xlabel("Weight")
plt.title("Weight Change by Age")
# another example
x = np.arange(0, 5, 0.1)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)
# CUSTOMIZATION
numpyArray1 = np.linspace(0,10,20)
numpyArray2 = numpyArray1**3
"""
plt.plot(array1,array2,"g--")
# now let's see two graphs on the same screen
plt.subplot(1,2,1) # 1st graph out of 2 graphs in 1 row
plt.plot(array1,array2,"g--") # this graph goes to the position given in the previous line
plt.subplot(1,2,2)
plt.plot(array1,array2,"g*-")
# figure
myFigure = plt.figure() # created an instance
# here 0.2 is the starting point of the left axis, 0.2 is the starting point of the bottom axis
figureAxes = myFigure.add_axes([0.4,0.4,0.6,0.6]) # last two indices are width and height values
figureAxes.plot(array1,array2,"g") # array start
# Other operations
figureAxes.set_xlabel("X Axis Data Name")
figureAxes.set_ylabel("Y Axis Data Name")
figureAxes.set_title("Graph Title")
"""
# CUSTOMIZATION 2
"""
figure2 = plt.figure()
# in the line below, the first 0.1 value determines the graph's position on the x axis
# and the second 0.1 determines the graph's position on the y axis
axis1 = figure2.add_axes([0.1,0.1,0.7,0.7])
axis2 = figure2.add_axes([0.3,0.3,0.3,0.3])
axis1.plot(array1,array2,"b")
axis1.set_xlabel("X Axis")
axis1.set_ylabel("Y Axis")
axis1.set_title("Main Graph Title")
axis2.plot(array2,array1,"b")
axis2.set_xlabel("Small X Axis")
axis2.set_ylabel("Small Y Axis")
axis2.set_title("Small Graph Title")
"""
# CUSTOMIZATION 3
"""
# if we didn't pass any values to subplots, the axes would be a tuple
(myFigure, axes) = plt.subplots(1,2)
print(type(axes)) # now this is an array
for axis in axes:
    axis.plot(array1,array2,"g")
    axis.set_xlabel("X Axis")
plt.tight_layout()
"""
# DETAILS AND SAVING THE FILE
"""
newFigure = plt.figure()
# dpi value can be given in the line above
graph = newFigure.add_axes([0.1,0.1,0.9,0.9])
graph.plot(array1,array1**2,label = "Square of the array")
graph.plot(array1,array2,label = "Cube of the array")
graph.legend(loc = 6)
newFigure.savefig("figure.png",dpi = 200) # value related to pixel quality
"""
# ADVANCED
# color usage
(newFigure, newAxis) = plt.subplots()
newAxis.plot(numpyArray1, numpyArray1 + 2, color="blue", linewidth = 1.0)
newAxis.plot(numpyArray1, numpyArray1 + 3, color ="yellow", linewidth = 1.0)
newAxis.plot(numpyArray1, numpyArray1 + 4, color = "#C96F23", linestyle = "-.")
newAxis.plot(numpyArray1, numpyArray1 + 5, color = "#C96F23", linestyle = ":")
newAxis.plot(numpyArray1, numpyArray1 + 6, color = "#C96F23", linestyle = "--")
newAxis.plot(numpyArray1, numpyArray1 + 7, color = "#000000", linestyle = "--", marker = "o",markersize = 8, markerfacecolor="red")
newAxis.plot(numpyArray1, numpyArray1 + 8, color = "#000000", linestyle = "-")
# SCATTER
plt.scatter(numpyArray1,numpyArray2)
# HISTOGRAM
newArray = np.random.randint(0,100,50)
plt.hist(newArray)
# BOXPLOT
plt.boxplot(newArray)
# We can go through the tutorials on the Matplotlib website
