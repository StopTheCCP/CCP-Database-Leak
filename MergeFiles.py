def MergeFiles(outputPath:str,*inputPaths:str):
    outputFile = open(outputPath, "a")
    for inputPath in inputPaths:
        for line in open(inputPath, "r"):
            outputFile.write(line)
    outputFile.close()