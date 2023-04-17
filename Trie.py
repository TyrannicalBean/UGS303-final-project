class Trie:
    
    def __init__(self):
        self.root = TrieNode('')

    def add(self, str):
        if(not str.isalpha()):
            print("String contains non-alphabet characters")
            return
        str = str.lower()
        self.root.add(str)
    
    def toList(self):
        return self.root.toList('')
    
    def __str__(self):
        return str(self.toList())



class TrieNode:
    def __init__(self, char:str):
        self.char = char
        self.links = []
        for i in range(27):
            self.links.append(None)
        self.end = False
        self.freq = 0
    
    def add(self, str):
        if(len(str) == 0):
            self.end = True
            self.freq+=1
        else:
            char = str[0]
            char_index = ord(char)-97
            node = self.links[char_index]
            if(node == None):
                self.links[char_index] = TrieNode(str[0])
                node = self.links[char_index]
            node.add(str[1:])
            
    def toList(self, prevStr:str):
        ret = []
        currentString = prevStr + self.char
        if(self.end):
            ret.append(currentString)
        for node in self.links:
            if node != None:
                ret.extend(node.toList(currentString))
        return ret

    def __str__(self):
        return self.char+": ("+str(self.freq)+")"

