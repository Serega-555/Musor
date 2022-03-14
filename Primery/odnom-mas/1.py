# 1.	Дан массив из 10 элементов. Элементы массива вводятся с клавиатуры.
# Написать программу, которая включает собственную функцию для замены всех четных элементов массива на 0.

class Mas:


    def input1(self):
        mas = []
        while len(mas) <= 9:
            mas.append(int(input("Введите данные => ")))
        return mas
    
    def mas(self):
        mas = Mas()
        b = mas.input1()
        print(b)
        for i in range(len(b)):
            if b[i] % 2 == 0:
                b[i] = 0
        print(b)

result = Mas()
result.mas()