import datetime
import binascii
import random

#Getting the current time
time=datetime.datetime.now()
timeString=str(time)

#Omitting redundant characters
timeString=timeString.replace("-","")
timeString=timeString.replace(":","")
timeString=timeString.replace(".","")
timeString=timeString.replace(" ","")

#Converting the string to binary string
binaryNumber=bin(int(binascii.hexlify(timeString),16))
binaryNumber = binaryNumber[2:]
randomLength=len(binaryNumber)

#Creating a list to contain the binary values 0 and 1
randomNumbers = [0,1]
padString=""

#Iterating for timeString length number of times, selecting randomly out of randomNumbers list
for x in range(1, randomLength):
    randomNumber=random.choice(randomNumbers)
    padString=padString+str(randomNumber)

#Padding the two binary strings
finalString = int(binaryNumber,2) ^ int(binaryNumber,2)
finalString = str(finalString)[2:]

#Finally printing the randomly generated binary string
print finalString



