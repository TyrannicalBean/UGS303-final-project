class Trie:
    
    def __init__(self):
        self.root = TrieNode('')

    def add(self, str):
        str = str.lower()
        self.root.add(str)
    
    def toList(self):
        return self.root.toList('')
    
    def getFreq(self, str):
        self.root.getFreq(str)
    
    def __str__(self):
        ret = ""
        words = sorted(self.toList(), key = lambda x: x[1], reverse = True)
        for word in words:
            ret += f"{word[0]:<30}:{word[1]}\n"
        return ret



class TrieNode:
    def __init__(self, char:str):
        self.char = char
        self.links = {}
        self.freq = 0
    
    def add(self, str):
        if(len(str) == 0):
            self.freq+=1
        else:
            char = str[0]
            try:
                node = self.links[char]
            except KeyError:
                node = self.links[char] = TrieNode(char)
            node = self.links[char]
            node.add(str[1:])
            
    def toList(self, prevStr:str):
        ret = []
        currentString = prevStr + self.char
        if(self.freq > 0):
            element = (currentString, self.freq)
            ret.append(element)
        for char in sorted(self.links.keys()):
                ret.extend(self.links[char].toList(currentString))
        return ret
    
    def getFreq(self, str):
        try:
            nextNode = self.links[str[0]]
            return nextNode.getFreq(str[1:])
        except KeyError:
            return 0

    def __str__(self):
        return f"{self.char} : {self.freq}"

