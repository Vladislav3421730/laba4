import math
class Triangle:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def check_on_exist(self):
        if self.a+self.b>self.c and self.a+self.c>self.b and self.b+self.c>self.a:
            return True
        else:
            return False
    def Square(self):
        if Triangle.check_on_exist(self) is False:
            print("Такого треугольника не существует")
        else:
            p=(self.a+self.b+self.c)/2
            print(f"Площадь треугольника {math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))}")

    def Perimetr(self):
        if Triangle.check_on_exist(self) is False:
            print("Такого треугольника не существует")
        else:
            print(f"Периметр тругольника {self.a+self.b+self.c}")

    def __str__(self):
        return (f"a={self.a},b={self.b},c={self.c}")
Tr1=Triangle(5,6,7)
Tr2=Triangle(1,8,9)
Tr3=Triangle(23,23,27)

print(Tr1)
Tr1.Perimetr()
Tr1.Square()

print(Tr2)
Tr2.Perimetr()
Tr2.Square()

print(Tr3)
Tr3.Perimetr()
Tr3.Square()
