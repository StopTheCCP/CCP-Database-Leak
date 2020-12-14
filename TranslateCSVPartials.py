import os
import time
# https://pypi.org/project/google-trans-new/
from google_trans_new import google_translator


# inputFileRange = [*range(1, 41)]  # all files from 1-40
inputFileRange = [1,2]  # specific files
inputFileBaseName = 'shanghai-ccp-member'
inputDir = f'Data/UntranslatedPartials'.replace('/', os.path.sep)
outputDir = f'Data/TranslatedPartials'.replace('/', os.path.sep)


def GetTimeString() -> str:
    t = time.localtime()
    return time.strftime('%H:%M:%S', t)


def ProcessFile(inputFilePath: str, outputFilePath: str):
    with open(outputFilePath, 'w', encoding='utf-8') as outputFile:
        with open(inputFilePath, 'r', encoding='utf-8') as inputFile:
            # n = line number
            n = 0
            for line in inputFile:
                n += 1
                if n % 1000 == 0:
                    currentTime = GetTimeString()
                    print(f'[{currentTime}] Processing row {n}')
                translatedText = TranslateCnToEn(line)
                outputFile.write(translatedText + '\n')


def TranslateCnToEn(textCn: str) -> str:
    # ref https://github.com/lushan88a/google_trans_new
    translator = google_translator(url_suffix='com')
    textEn = translator.translate(textCn.strip(), lang_src='zh', lang_tgt='en')
    return textEn


if __name__ == '__main__':
    time0 = time.time()
    if not os.path.exists(outputDir):
        os.mkdir(outputDir)

    for fileNumber in inputFileRange:
        fileName = f'{inputFileBaseName}_{fileNumber}.csv'
        inputFilePath = os.path.join(inputDir, fileName)
        outputFilePath = os.path.join(outputDir, fileName)

        # TODO: handle this better, but currently it's best to not overwrite anything and yell at user
        if os.path.exists(outputFilePath):
            raise RuntimeError(f'Output file already exists at {outputFilePath}') from None

        currentTime = GetTimeString()
        print(f'[{currentTime}] Processing File: {inputFilePath}')
        ProcessFile(inputFilePath, outputFilePath)

    timeN = time.time()
    durationMinutes = int((timeN - time0) / 60)
    print(f'Total Translation Minutes = {durationMinutes}')