class Country:
    def __init__(self,capital,Square,population):
        self.capital = capital
        self.Square = Square
        self.population = population
    def __str__(self):
        return (f"Столица - {self.capital}, площадь - {self.Square}, население - {self.population}")

France=Country("Париж", 1230000, 85000000)
Belarus=Country("Minsk",190000,9500000)
USA=Country("Vashington",3400000,35000000)
China=Country("Pekin",12212338782, 1500000000)
Spain=Country("Madrid",1233133,47000000)
ContryList=[France,Belarus,USA,China,Spain]
try:
    Square=int(input("Введите площадь : "))
    Population=int(input("Введите население : "))
except ValueError:
    print("Вы неправильно ввели числа")
print("Страны с заданной плозадью : ")
for el in ContryList:
    if el.Square==Square:
        print(el)
print("страны с зажанным населением : ")
for el in ContryList:
    if el.population==Population:
        print(el)

