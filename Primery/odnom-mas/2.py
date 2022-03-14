# 2.	Дан массив из 10 элементов. Элементы массива вводятся с клавиатуры.
# Написать программу, которая включает собственную функцию для нахождения суммы четных элементов массива.

class Mas:
    
    def _mas(self):
        mas = []
        while len(mas) <= 9:
            mas.append(int(input("Введите число массива => ")))
        return mas

    def _fun(self):
        a = 0
        for i in self.mas():
            if i % 2 == 0:
                a = a + i
        
        return a
    def printl(self):
        print("Сумма всех четных элементов = ", self.fun())

class Mas1(Mas):
    def liza(self):
        print(self.printl())

func = Mas1()
func.liza()