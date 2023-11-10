import time
class Dog:
    AGE_COEF:int = 7
    KIND:str = "cainie"
    N_EYES_DOG:int = 2
    N_LEGS_DOG:int = 5
    
    def __init__(self, name:str, owner:str, age:int) -> None:
        self.name:str = name
        self.age:int = age
        self.owner = owner
    
    def convert_age(self)->int:
        return self.age * Dog.AGE_COEF
    
    def talk(self)->None:
        print(f"{self.name} says woff and my age is {self.convert_age()}!!")
    
    def play_fetch(self, throws:int)->None:
        for _ in range(0,throws):
            print(f"{self.owner} throws the ball!")
            time.sleep(1)
            print(f"{self.name} catches the ball and returns it")
            time.sleep(.2)
            
        
if __name__ == "__main__":
    myDog = Dog("Ralf","Owner", 5)
    myDog.talk()
    myDog.play_fetch(5)