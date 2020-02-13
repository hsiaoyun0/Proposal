import os
import argparse

# initial
parser = argparse.ArgumentParser()
parser.add_argument('--numberoffile', type=int, default=100)

def ReadFile():
    #Read File Name
    CNNFileName = os.listdir("/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories")

    # Read File
    for filename in CNNFileName :
        filename = '/share/corpus/CNN_DailyMail/CNN_DailyMail/origin(DMQA)/cnn/stories/'+ filename
        f = open(filename, "r")
        print(f.read())


def __init__(self, needamount):
    self.needamount = needamount


if __name__ == '__main__':
    args = parser.parse_args()
    print(args.numberoffile)
