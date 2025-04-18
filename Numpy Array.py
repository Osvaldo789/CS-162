import numpy as np #imports numpy for use

myArray = np.random.randint(0, 20, size=(5, 5)) #Creates myArray with a 5x5 grid with numbers ranging from 0-20

print(myArray) #Prints the entire array

print(myArray[1,2]) #Prints number found in second row, third column

print(np.sum(myArray)) #Prints sum of entire array

print(np.mean(myArray, axis=1)) #Prints mean of each row in the array

print(np.max(myArray, axis=0)) #Prints max value in each column of array