import os
import argparse
import re

# initial
parser = argparse.ArgumentParser()
parser.add_argument('--numberoffile', type=int, default=100)
parser.add_argument('--numberofans', type=int, default=3)

def ReadFile(numberoffile):
    
    getnum = numberoffile
    #Read File Name
    CNNFileName = os.listdir("/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories")
    if len(CNNFileName)<getnum:
        getnum = len(CNNFileName)

    # Read File
    NeedFile=[]
    for filename in CNNFileName[:getnum] :
        content= ""
        filename = '/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories/'+ filename
        content = list(filter(None, re.split('[.?\n]',open(filename, "r").read())))

        NeedFile.append(content)

    return NeedFile

def ProduceAnswer(FileContent, numberofans):
    
    DocumentPair=[]
    flag = FileContent[0].count("@highlight")
    
    if flag < numberofans:
        numberofans = flag
    
    for Content in FileContent:
        ans=[]
        context=[]
        for Sen in Content[-(flag*2):-(flag-numberofans)]:
            if Sen != "@highlight":
                ans.append(Sen)
        
        for Sen in Content:
             if Sen == "@highlight": break
             context.append(Sen)
        
        DocumentPair.append([context,ans])
     
    return DocumentPair

def MakeFile(args, DocumentPair):
    FileName = "CNN_"+str(args.numberofans)+"ans_"+str(args.numberoffile)+"files.txt"
    with open(FileName,"w") as Writein :
        for Pair in DocumentPair:
            Writein.write("Story\n")
            for Sen in Pair[0] :
                Writein.write(Sen)
            Writein.write("\nAnswer\n")
            for Sen in Pair[1]:
                Writein.write(Sen)
                Writein.write(" ")
            Writein.write("\n\n")

if __name__ == '__main__':
    args = parser.parse_args()
    FileContent = ReadFile(args.numberoffile)
    DocumentPair = ProduceAnswer(FileContent, args.numberofans)
    MakeFile(args, DocumentPair)    
