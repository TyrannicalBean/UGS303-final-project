import os
from Person import Person

def prune():
    inPath = ".\outputs\outputs"
    outPath = ".\outputs\pruned"
    files = os.listdir(inPath)
    for file in files:
        inFileName = inPath+"\\"+file
        outFileName = outPath + "\\" + file[0:-4]+"pruned.txt"
        __prune(inFileName, outFileName)


def __prune(inFileName, outFileName):
    inFile = open(inFileName, 'r', encoding='utf-8')
    outFile = open(outFileName, 'w', encoding='utf-8')
    for i in range(3):
        line = inFile.readline()
        outFile.write(line)
    for line in inFile.readlines():
        try:
            str = line[line.rindex('[') : line.rindex(']') + 1]
            name, age, race, gender = str[1:-1].split(",")
            name = name.removeprefix("name:").strip(' \"')
            age = int(age.removeprefix("age:").strip(' \"'))
            race = race.removeprefix("race:").strip(' \"')
            gender = gender.removeprefix("gender:").strip(' \"')
            person = Person(name, age, race, gender)
            outFile.write(f"{person}\n")
        except ValueError:
            continue
    inFile.close()
    outFile.close()

if __name__ == '__main__':
    prune()
