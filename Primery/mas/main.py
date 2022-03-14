masList = [1, 2, 3, 4, 5]
mas = ["Привет", "это элемент"]
print(masList)

masList.append(15)  # Добавляет в конец списка число 15
masList.extend(mas) # Расширяет список masList списком mas
masList.insert(0, 5) # Добавляет число 5 в индекс 0 при этом весь список смещается на +1
masList.remove(1)    # Удаляет число под индексом 1 при этом список смещается на -1
print(masList.pop(2)) # Удаляет элемент под инднксом 2 и возвращает его значение
print(masList)        

masList.reverse()   # Разворачивает список
print(masList)

masList.clear()    # Очищает список
print(masList)