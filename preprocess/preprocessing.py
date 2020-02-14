import os
import argparse
import re

# initial
parser = argparse.ArgumentParser()
parser.add_argument('--numberoffile', type=int, default=100)
parser.add_argument('--numberofans', type=int, default=3)
parser.add_argument('--source', type=str, default='cnn', help='cnn | dailymail')

def ReadFile(source, numberoffile):
    
    getnum = numberoffile
    source = "/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/"+source+"/stories"
    #Read File Name
    CNNFileName = os.listdir(source)
    if len(CNNFileName)<getnum:
        getnum = len(CNNFileName)

    # Read File
    NeedFile=[]
    for filename in CNNFileName[:getnum] :
        content= ""
        filename = source+"/"+ filename
        content = list(filter(None, re.split('[.?\n]',open(filename, "r").read())))
        NeedFile.append(content)

    return NeedFile

def StartEndPoints(Content, numberofans):
    
    flag = Content.count("@highlight")
    if flag < numberofans :
        numberofans = flag
    start = Content.index("@highlight")
    end=0
    if flag == numberofans:
        end = len(Content)-1
    else:
        allindex=[]
        i=0
        for Sen in Content[start:]:
            #print(Sen)
            if Sen == "@highlight":
                allindex.append(i+start)
            i+=1
        end=int(allindex[numberofans])
        
    return start, end
     

def ProduceAnswer(FileContent, numberofans):
    
    DocumentPair=[]
    
    for Content in FileContent:
        ans=[]
        context=[]
        start, end = StartEndPoints(Content, numberofans)

        for Sen in Content[start:end]:
            if Sen != "@highlight":
                ans.append(Sen)
        for Sen in Content:
             if Sen == "@highlight": break
             context.append(Sen)
        
        DocumentPair.append([context,ans])
     
    return DocumentPair

def MakeFile(args, DocumentPair):
    FileName = str(args.source)+"_"+str(args.numberofans)+"ans_"+str(args.numberoffile)+"files.txt"
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
    FileContent = ReadFile(args.source, args.numberoffile)
    DocumentPair = ProduceAnswer(FileContent, args.numberofans)
    MakeFile(args, DocumentPair)    
