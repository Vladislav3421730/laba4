from abc import abstractmethod
class Vehicle:
    def __init__(self,StartCity,FinalCity,Distance,time,Coast):
        self.StartCity=StartCity
        self.FinalCity=FinalCity
        self.time=time
        self.Distance=Distance
        self.Coast=Coast
    @abstractmethod
    def WayMovement(self):
        pass
    def __str__(self):
       return(f"Пункт посадки - {self.StartCity}\nПункт прибытия - {self.FinalCity}\nДистанция - {self.Distance}\n"
              f"Время - {self.time}\nЦена - {self.Coast}")
    def getTime(self):
        return self.time
    def getCoast(self):
        return self.Coast
    def ForWriting(self):
        return f"{self.StartCity} {self.FinalCity} {self.Distance} {self.time} {self.Coast}\n"


class Plain(Vehicle):
    def WayMovement(self):
        print("Перемещение идёт при помощи самолёта")

class Train(Vehicle):
    def WayMovement(self):
        print("Перемещение идёт при помощи поезда")
class Car(Vehicle):
    def WayMovement(self):
        print("Перемещение идёт при помощи машины")


plain1=Plain("Минск","Москва", 1300, 4, 300)
plain2=Plain("Москва","Париж",5600,6,700)
train1=Train("Минск","Барановичи",260,4,12)
train2=Train("Гродно","Брест",260,3,9)
car1=Car("Гродно","Зельва",170,2,30)
car2=Car("Могилёв","Витебск",340,3,4)

TransportList=[plain1,plain2,train1,train2,car1,car2]

print("Самая быстрая поездка")
print(min(TransportList,key=Vehicle.getTime))
print()
print("Самая экономичная поездка")
print(min(TransportList,key=Vehicle.getCoast))

with open("Transport.txt",'w',encoding='utf-8') as file:
     for el in TransportList:
        file.write(el.ForWriting())

