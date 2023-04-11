# MATPLOTLIB LIBRARY EXAMPLES


# plotting a graph
import matplotlib.pyplot as plt
plt.plot([1,2,3],[1,2,3])
plt.show()

# plotting a graph with headers marked as label() function
import matplotlib.pyplot as plt
X=[1,4,8]
Y=[9,4,1]
plt.plot(X,Y)
plt.title("info")
plt.Ylabel("Y-axis")
plt.Xlabel("Y-axis")
plt.show()

# plotting graph by changing figure size by figure() function
import matplotlib.pyplot as plt
plt.plot([1,4,7],[4,3,7])
plt.figure(figsize=(100,120))
plt.show()

# matplotlib subplot by subplot() function
import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.plot([1,2,3],[3,2,1])
plt.title('1st subplot')

plt.subplot(1,2,2)
plt.plot([9,5,2],[3,4,2],"r^")
plt.title('1st subplot')
plt.show()

# add_subplot() adding a graph inside a graph
import matplotlib.pyplot as plt
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)
ax1.plot([1,2,3])
ax2=fig.add_subplot(2,2,1,facecolor='w')
ax2.plot(1,2,0.5)


#  bar graph
import matplotlib.pyplot as plt
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
section=['Div-A','Div-B','Div-C','Div-D','Div-E']
students=[23,21,19,34,32]
plt.title('Result')
plt.xlabel('section')
plt.ylabel('no. of students')
ax.bar(section,students)
plt.show()

# histogram
import matplotlib.pyplot as plt
import numpy as np
ax=fig.add_axes([0,0,1,1])
fig,ax=plt.subplots(1,1)
a=np.array([12,34,54,32,89,78,54,65])
ax.hist(a, bins='auto')
ax.set_title("Histogram")
ax.set_xlabel("Marks")
ax.set_xlabel("Students")
plt.show()

# scatter plot
import matplotlib.pyplot as plt
girls_grade=[86,74,63,56,87,98,45,24,34,56]
boys_grade=[83,34,53,16,97,88,43,54,94,59]
grades_range=[10,20,30,40,50,60,70,80,90,100]
fig=plt.figure()
ax=fig.add_axes([0,0,1,1])
ax.scatter(grades_range,girls_grade,color='r')
ax.scatter(grades_range,boys_grade,color='b')
ax.set_xlabel("grades range")
ax.set_ylabel("grades scored by students")
ax.set_title("scatter plot")
plt.show()

# 3d projection
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax= plt.axes(projection = '3d')

# 3 dimensional line graph
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax=plt.axes(projection='3d')

z=np.linspace(0,1,100)
x=z*np.sin(25*z)
y=z*np.cos(25*z)

ax.plot3D(x,y,z,'green')
ax.set_title('3d line plot')
plt.show()

# 3 dimensional scattering graph

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax=plt.axes(projection='3d')

z=np.linspace(0,1,100)
x=z*np.sin(25*z)
y=z*np.cos(25*z)
ax.scatter(x,y,z,'green')


ax.set_title('3d line plot')
plt.show()
