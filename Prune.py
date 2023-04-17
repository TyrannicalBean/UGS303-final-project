
def prune():
    for fileNum in range(13)[1:]:
        inFileName = 'outfile'+str(fileNum)+'.txt'
        outFileName = 'pruned'+str(fileNum)+'.txt'
        infile = open(inFileName,'r', encoding='utf-8')
        outfile = open(outFileName, 'w', encoding='utf-8')
        for i in range(3):
            line = infile.readline()
            outfile.write(line)
        for line in infile.readlines():
            if "[" in line:
                outfile.write(line)

def prune(inFileName, outFileName):
    inFile = open(inFileName, 'r', encoding='utf-8')
    outFile = open(outFileName, 'w', encoding='utf-8')
    for i in range(3):
        line = inFile.readline()
        outFile.write(line)
    for line in inFile.readlines:
        if "[" in line:
            outFile.write(line)

if __name__ == '__main__':
    prune()
