import numpy as np
import matplotlib.pyplot as plt

#Read elevation data into an array
elevations = np.loadtxt('elevationsNYC.txt') #read data to array (CONVERTS DATA TO NUMPY)
plt.imshow(elevations)                       #load the arry to plt
plt.show()                                   #display the plot

#makes a new image called mapShape
#elevation.shape returns (row & columns)
mapShape = elevations.shape + (3,) #adds dimension to the image
floodMap = np.zeros(mapShape)      #create an blank image

for row in range(mapShape[0]):          #goes over each row
    for col in range(mapShape[1]):      #goes over each col
        if elevations[row,col] <= 0:    #water areas
            floodMap[row,col,2] = 1.0   #makes it blue
        elif elevations[row,col] <= 6:  #flood area
            floodMap[row,col,0] = 1.0   #makes it red
        else:                           #normal
            floodMap[row,col,1] = 1.0   #makes it green

plt.imshow(floodMap)                    #displays the image
plt.show()                              #shows it duh
plt.imsave('floodMap.png', floodMap)    #saves it as img (name of file, what array)
