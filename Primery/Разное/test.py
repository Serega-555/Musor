print("Введите год для определения высокостного года => ")
print("Начало с 1904 года")
print()

def vis_god(god):
    print()

god = int(input("Введите год => "))

if god % 2 == 1:
    print("Год не высокостный")
elif god < 1904 and god > 2100:
    print("Год слишком далекий.")
else:
    print(vis_god(god))
