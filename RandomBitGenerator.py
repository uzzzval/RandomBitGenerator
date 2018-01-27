import datetime
import binascii
import random

time=datetime.datetime.now()
timeString=str(time)

timeString=timeString.replace("-","")
timeString=timeString.replace(":","")
timeString=timeString.replace(".","")
timeString=timeString.replace(" ","")


binaryNumber=bin(int(binascii.hexlify(timeString),16))
binaryNumber = binaryNumber[2:]
randomLength=len(binaryNumber)
randomNumbers = [0,1]
padString=""
for x in range(1, randomLength):
    randomNumber=random.choice(randomNumbers)
    padString=padString+str(randomNumber)

print padString

finalString = int(binaryNumber,2) ^ int(binaryNumber,2)
finalString = str(finalString)[2:]

print finalString
