"""
class-> Entity

Example: Dog, Cat

"""

class Animal:
    def __init__(self,*args):
        if len(args)==1:
            self.name=args[0]
        if len(args)==2:
            self.name=args[0]
            self.age=args[1]
        if len(args)==3:
            self.name=args[0]
            self.age=args[1]
            self.species=args[2]
        

class Car:
    def __init__(self,window, door, fuel ):
        self.window=window
        self.door=door
        self.fuel=fuel

class Maruti(Car):
    def __init__(self, window, door, fuel, model):
        super().__init__(window, door, fuel)
        self.model=model


if __name__=="__main__":
   alto=Maruti(8,5,"petrol","Alto")
   print(alto.door)
   print(alto.model)
   