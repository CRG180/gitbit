
class Dog:
    AGE_COEF:int = 7
    KIND:str = "cainie"
    N_EYES_DOG:int = 2
    N_LEGS_DOG:int = 5
    
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