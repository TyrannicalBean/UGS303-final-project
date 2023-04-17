class Person:

    def __init__(self, name:str, age:int, race:str, gender:str):
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
    
    def __str__(self):
        return self.name + ": ("+self.age+", "+self.race+", "+self.gender+")"