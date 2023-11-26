from abc import abstractmethod
class Figure:
    def __init__(self,a=4,b=5):
        self.a=a
        self.b=b
    @abstractmethod
    def FindPerimetr(self):
        pass
    @abstractmethod
    def Square(self):
        pass
    def __str__(self):
        return (f"Сторона 1- {self.a} сторона 2 - {self.b}")
class Kvadrat(Figure):
    def __init__(self,a,b):
        super().__init__(a,b)
    def FindPerimetr(self):
        return 2*(self.a+self.b)
    def Square(self):
        return self.a*self.b
