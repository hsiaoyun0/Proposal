import os
import argparse
import re

# initial
parser = argparse.ArgumentParser()
parser.add_argument('--numberoffile', type=int, default=100)

def ReadFile(numberoffile):
    
    getnum = numberoffile
    #Read File Name
    CNNFileName = os.listdir("/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories")

    # Read File
    NeedFile=[]
    for filename in CNNFileName[:getnum] :
        content= ""
        filename = '/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories/'+ filename
        content = list(filter(None, re.split('[.?\n]',open(filename, "r").read())))

        NeedFile.append(content)

    return NeedFile


if __name__ == '__main__':
    args = parser.parse_args()
    FileContent = ReadFile(args.numberoffile)
    print(FileContent)
