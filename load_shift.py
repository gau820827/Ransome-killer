""" Load the data into 1500 columns vector and shift to the center """
from settings import *


MTU = 1500

def loadIntoVector(feature):
    """Load the extraction payload into a 1500 columns vector
    
    @param feature: the extraction payload, for instance GET HTTP1.1

    @returns: A 1500 columns vector
    """


    datas = [ x for x in feature.split(",") if x != ""]
    if len(datas) > MTU:
        datas = datas[:MTU]
    shift = (MTU - len(datas))/2
    vector = 1500*["0"]
    for data in datas:
        vector[shift] = str(data)
        shift += 1
    return vector


def dataHandler(inputFileName, inputDataName):
    """Read original datas, make them standardization,
    and produce XXX.in and XXX.out
    
    @param  inputFileName: the raw payload data
            inputDataName: the name you want to save as XXX.in,
                           also will be saved as XXX.out

    @returns: None
    """


    with open(inputFileName, "r") as inputFile:
        while True:
            line = inputFile.readline()
            if not line: break
            

            vector = loadIntoVector(line.strip())
            with open(inputDataName, "a") as inputDataFile:
                inputDataFile.write(','.join(vector))
                inputDataFile.write("\n")
                """ Write label """
                cat = -1
                if "train" in inputFileName:
                    cat = 0
                elif "test" in inputFileName:
                    cat = 1
                if "normal" in inputFileName:
                    with open(outputLabelName[cat], "a") as outputLabelFile:
                        outputLabelFile.write("0" + "\n")
                elif "malware" in inputFileName:
                    with open(outputLabelName[cat], "a") as outputLabelFile:
                        outputLabelFile.write("1" + "\n")


""" Create files if not exist """
for name in outputDataName:
    open(name, 'w')
for name in outputLabelName:
    open(name, "w")


""" Handle training data """
dataHandler(inputMalName[0], outputDataName[0])
dataHandler(inputNorName[0], outputDataName[0])


""" Handle testing data """
dataHandler(inputMalName[1], outputDataName[1])
dataHandler(inputNorName[1], outputDataName[1])