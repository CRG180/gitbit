
class Dog:
    AGE_COEF = 7
    KIND = "cainie"
    
    def __init__(self, name:str, age:int) -> None:
        self.name:str = name
        self.age:int = age
    
    def convert_age(self)->int:
        return self.age * Dog.AGE_COEF
    
    def talk(self)->None:
        print(f"{self.name} says woff and my age is {self.convert_age()}!!")
        
if __name__ == "__main__":
    myDog = Dog("Ralf", 5)
    myDog.talk()