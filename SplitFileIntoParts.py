import os

def CleanupOutputDirectory(inputFilePath, outputDir):
    inputFileName = os.path.basename(inputFilePath)
    inputFileNameBase = inputFileName.split('.')[0]
    for (directoryPath, subdirectoryList, fileList) in os.walk(outputDir):
        for fileNameSingle in fileList:
            if fileNameSingle.endswith('.csv') and fileNameSingle.startswith(inputFileNameBase):
                os.remove(os.path.join(outputDir, fileNameSingle))
                
def SplitFileIntoParts(inputPath:str, outputDir:str = None, maxNumFiles:int=1, maxLinesPerFile:int=None):
    cnt = 0
    fileNumber = 1
    inputPath = os.path.abspath(inputPath)
    fileName, ext = os.path.basename(inputPath).rsplit('.',maxsplit=1)

    # if an output directory is specified, use that as the base, otherwise use input directory
    if outputDir != None:
        outputFileBase = os.path.join(outputDir, fileName)
        print(outputFileBase)
    else:
        inputPathDir = inputPath.rsplit(os.path.sep,maxsplit=1)[0]
        outputFileBase = os.path.join(inputPathDir, fileName)
        print(outputFileBase)
    
    # if a maxNumFiles is specified, determine how many lines per file
    if maxLinesPerFile != None and maxLinesPerFile > 0:
        maxNumFiles = 0
    if maxNumFiles > 0:
        chunkSize = 8192 * 1024
        breakCount = 0
        with open(inputPath, 'rb') as inputFile:
            while True:
                buffer = inputFile.read(chunkSize)
                if not buffer:
                    break
                breakCount += buffer.count(bytes('\n', encoding='utf8'))
        maxLinesPerFile = float(breakCount) / float(maxNumFiles)
        if maxLinesPerFile.is_integer:
            maxLinesPerFile = int(maxLinesPerFile)
        else:
            maxLinesPerFile = int(maxLinesPerFile) + 1

    # process input file
    outputFile = open("{}_{}.{}".format(outputFileBase,fileNumber,ext), "w", encoding='utf8')
    for line in open(inputPath, "r", encoding='utf8'):
        cnt += 1
        outputFile.write(line)
        if(cnt % maxLinesPerFile == 0):
            outputFile.close()
            if maxNumFiles != fileNumber:
                fileNumber += 1
                outputFile = open("{}_{}.{}".format(outputFileBase,fileNumber,ext), "w", encoding='utf8')
    outputFile.close()

if __name__ == "__main__" :
    inputFilePath = f'Data/shanghai-ccp-member.csv'
    outputDir = f'Data/UntranslatedPartials'
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)
    CleanupOutputDirectory(inputFilePath, outputDir)
    SplitFileIntoParts(inputFilePath, outputDir=outputDir, maxLinesPerFile=50000)