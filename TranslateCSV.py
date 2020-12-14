import os
import time
# https://pypi.org/project/google-trans-new/
from google_trans_new import google_translator

def TranslateCnToEn(textCn:str) -> str:
    # ref https://github.com/lushan88a/google_trans_new
    translator = google_translator(url_suffix='us')
    textEn = translator.translate(textCn.strip(), lang_src='zh', lang_tgt='en')
    return textEn

def ProcessFile(inputFilePath:str, outputFilePath:str):
    with open(outputFilePath, 'w', encoding='utf-8') as outputFile:
        with open(inputFilePath, 'r', encoding='utf-8') as inputFile:
            # n = line number
            n = 0
            for line in inputFile:
                n += 1
                if n % 1000 == 0:
                    t = time.localtime()
                    currentTime = time.strftime('%H:%M:%S', t)
                    print(f'[{currentTime}] Processing row {n}')
                translatedText = TranslateCnToEn(line)
                outputFile.write(translatedText + '\n')

if __name__ == '__main__':
    time1 = time.time()
    inputFilePath = 'Data/shanghai-ccp-member.csv'
    outputFilePath = 'Data/shanghai-ccp-member-en.csv'
    if os.path.exists(outputFilePath):
        os.remove(outputFilePath)
    ProcessFile(inputFilePath, outputFilePath)
    time2 = time.time()
    duration = time2 - time1
    print(f'Translation seconds = {duration}')