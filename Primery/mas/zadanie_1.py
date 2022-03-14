# Создать класс Car (автомобиль). Автомобиль имеет следующие данные: 
# - модель (Honda, BMW, др.)
# - год выпуска (1995, 2000, др.)
# - пробег (в км)
# - цвет (синий, белый, др.)

# Типы и имена переменных определить самим.

# Класс должен иметь несколько конструкторов. Различные конструкторы могут принимать разное количество параметров. 

# Например:
# - Один конструктор имеет только параметры модели и цвета. В этом случае, остальные данные присваиваются по умолчанию: год – 2009; пробег – 0 км, и др. 
# - Другой конструктор может иметь параметры для всех данных. 

# Класс имеет следующие методы:
# - getPrice() возвращает стоимость автомобиля (в USD) в зависимости от параметров. Формулу расчета определить самим. 
# - printAllInfo() – печатает все данные автомобиля, включая стоимость. 
# - printShortInfo() – печатает только краткую информацию: модель, год и цена.  

# Создайте несколько объектов, используя данный класс. 

class Car:

    def __init__(self, model, age, lends = "0", color = "0"):
        self.model = model
        self.age = age
        self.lends = lends
        self.color = color

    
    def getPrize(self):
        if type(self.lends) == int:
            print("Цена ", len(self.model) * self.age + self.lends + len(self.color))
        else:
            print("Все или один из параметров не указаны")

    def printAllInfo(self):
        print("Модель ", self.model)
        print("Год выпуска ", self.age)
        print("Пробег ", self.lends)
        print("Цвет ", self.color)
        self.getPrize()

    def printShortInfo(self):
        print("Модель ", self.model)
        print("Год выпуска ", self.age)
        self.getPrize()
car1 = Car("Mercedes", 2005, 2000, "red")
car1.getPrize()
print("------------------------------")
car1.printAllInfo()
print("------------------------------")
car1.printShortInfo()