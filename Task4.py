class Product:
    total_product=0
    def __init__(self, Name, Price , Amount):
        self.Name=Name
        self.Price=Price
        self.Amount=Amount
        Product.total_product=Product.total_product+1
    def __str__(self):
        return (f"Название - {self.Name}, цена - {self.Price}, количество - {self.Amount}")
    def __eq__(self, other):
        return self.Name==other
    def __isub__(self, other):
        self.Amount-=other
        return self
    def WorWriting(self,Amount=1):
        return (f"Название - {self.Name}, цена - {self.Price}, количество - {Amount}")
    @staticmethod
    def ViewAmountOfProducts():
        print(f"Количество товаров {Product.total_product}")

pr1=Product("Игрушка",6,7)
pr2=Product("Кружка",8,15)
pr3=Product("Ковёр",20,16)
pr4=Product("Цветок",18,23)
pr5=Product("Лопата", 14,3)
ListProduct=[pr1,pr2,pr3,pr4,pr5]
for el in ListProduct:
    print(el)
Product.ViewAmountOfProducts()
ProductName=input("Введите название товара которое вы хотите купить : ")
Result=True
for el in ListProduct:
    if ProductName==el:
        Result=False
        try:
            ProductAmount=int(input("Введите количество товара : "))
            if el.Amount-ProductAmount>=0:
                el-=ProductAmount
                print("Товар куплен, информация ниже")
                print(el)
                with open("Product.txt",'w',encoding='utf-8') as file:
                    file.write(el.WorWriting(ProductAmount))
            else:
                print("Нет такого количества товара")
        except ValueError:
            print("Неправильно введено значение")
if Result:
    print("Нет такого товара")
