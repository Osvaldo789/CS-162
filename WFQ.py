from queue import Queue #imports queue for use in program

#Creates 3 different queues. Economy, Standard, and Premium
eQueue = Queue()
sQueue = Queue()
pQueue = Queue()

myFile = open("input queue-1.txt", "r") #Opens .txt file containing the list data

data = myFile.read() #Stores myFile into variable data

inputData = data.split("\n") #Creates a list making a new entry for every line
myFile.close() #Closes open file
print(inputData) #Print to verify items successfully added to list


for l in inputData: #Iterates through each list item in inputData
    if l.startswith("E"): #If current string starts with "E", add to eQueue
        eQueue.put(l[2:]) #Only adds the name and not the priority letter
    if l.startswith("S"): #If current string starts with "S", add to sQueue
        sQueue.put(l[2:])
    if l.startswith("P"): #If current string starts with "P", add to pQueue
        pQueue.put(l[2:])

#Print to check proper enqueueing
print(list(eQueue.queue))
print(list(sQueue.queue))
print(list(pQueue.queue))

while eQueue.qsize() != 0 or sQueue.qsize() != 0 or pQueue.qsize() != 0: #Runs as long as one of the queues has people left
    if pQueue.qsize() != 0: #Checks if Premium queue is empty, then tries 2 more times before moving to Standard
        print(pQueue.get_nowait())
        if pQueue.qsize() != 0:
            print(pQueue.get_nowait())
            if pQueue.qsize() != 0:
                print(pQueue.get_nowait())
    if sQueue.qsize() != 0: #Checks if Standard queue is empty, then tries 1 more time before moving to Economy
        print(sQueue.get_nowait())
        if sQueue.qsize() != 0:
            print(sQueue.get_nowait())
    if eQueue.qsize() != 0: #Checks if Economy queue is empty, then starts again from the top
        print(eQueue.get_nowait())