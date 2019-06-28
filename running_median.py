
import os.path
import sys

def processInputFile(fileName):
    if os.path.exists(fileName):
        getInputList = [inputLine.rstrip('\n') for inputLine in open(fileName)]
        processedIntResultList = list(map(int, getInputList))
        processedIntResultList.sort()
        new_list = []
        for i in processedIntResultList:
            new_list.append(i)
            print ("{:.1f}".format(runningMedian(new_list)))
    else:
        raise Exception('{} provided does not exists'.format(fileName))

def runningMedian(runningList):
    length = len(runningList)
    isOdd = (length % 2) == 0
    if isOdd:
        index = int(length/2)
        value = (runningList[index]+ runningList[index-1]) / 2
    else: 
        if length == 1:
            value = runningList[0]
        else:
            index = int((length + 1) /2)
            value =runningList[index-1]
    return value

processInputFile(sys.argv[1])

