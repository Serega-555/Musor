# class A:
#     def __init__(self, kol):
#         self.kol = kol


#     def inputMas(self):
#         mas = []
#         while len(mas) <= self.kol - 1:
#             mas.append(int(input("Введите цифру>>  ")))
#         return mas

#     def printMas(self):
#         print("Сумма = ", self.suma)
#         print("Произведение = ", self.proizvedenie)
        
        
# class B(A):
#     def __init__(self, kol):
#         A.__init__(self, kol)

#     def summa(self):
#         suma = 0
#         proizvedenie = 1
#         for i in self.inputMas():
#             suma += i
#             proizvedenie *= i
#         return suma, proizvedenie


# kol = int(input("Сколько букв в вашей фамилии >>  "))
# m = B(kol)
# m.summa()
