class Person:

    def __init__(self, name:str, age:int, race:str, gender:str):
        if type(age) is not int:
            raise ValueError('age is not an int')
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
    
    @staticmethod
    def getPerson(str:str)->'Person':
        name, age, race, gender = [x.strip() for x in str[1:-2].split(',')]
        age = int(age)
        return Person(name, age, race, gender)

    def __str__(self):
        return f"[{self.name}, {str(self.age)}, {self.race}, {self.gender}]"