# """
# Private Access
# """
# class Person:
#     def __init__(self, name, age):
#         self._name=name
#         self._age=age
# class Rem(Person):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#     def display(self):
#         print(f"{self.name} is {self.age} years old")
# if __name__=="__main__":
#     person_test= Rem(name= "Ram", age=22)
#     print(person_test.display)
from abc import ABC, abstractmethod
class BankingApp:
    def database(self):
        print(f"Connected to Database Successfully.")
    @abstractmethod
    def security(self):
        pass
class MobileApp(BankingApp):
    pass

if __name__=="__main__":
    app=MobileApp()
    
    