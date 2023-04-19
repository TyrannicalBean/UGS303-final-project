import os
from Trie import Trie
from Person import Person
from collections import defaultdict

def stats(inPath, outPath):
    for file in os.listdir(inPath):
        inFile = open(f'{inPath}\{file}', 'r', encoding='utf-8')
        outFile = open(f'{outPath}\{file}', 'w', encoding='utf-8')
        stat(inFile, outFile)
        inFile.close()
        outFile.close()

def def_value():
    return 0

def stat(inFile, outFile):
    for i in range(3):
        line = inFile.readline()
        outFile.write(f'{line}\n')
    nameTrie = Trie()
    raceTrie = Trie()
    genderTrie = Trie()
    ageStat = defaultdict(def_value)
    for line in inFile.readlines():
        person = Person.getPerson(line)
        nameTrie.add(person.name)
        ageStat[person.age] += 1
        raceTrie.add(person.race)
        genderTrie.add(person.gender)
    outFile.write(str(nameTrie))
    outFile.write('\n\n\n')
    for age in sorted(ageStat.keys()):
        outFile.write(f'age {age}: {ageStat[age]}\n')
    outFile.write('\n\n\n')
    outFile.write(str(raceTrie))
    outFile.write('\n\n\n')
    outFile.write(str(genderTrie))



if __name__ == '__main__':
    stats('outputs\pruned', 'outputs\stats')
