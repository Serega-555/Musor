print()
print("What you want know? (amperage, voltage, resistance)")
print("amperage = 1")
print("voltage = 2")
print("resistance = 3")
# Выбираем что рассчитать
while True:
    want = float(input("I want know: "))
    if want == 1 or want == 2 or want == 3:
        break
    else:
        print("NO, onky 1 to 3")
# Calculation process 
def amper(voltage, resistance):
    return voltage / resistance
def volt(amperage, resistance):
    return amperage * resistance
def om(amperage, voltage):
    return voltage / amperage

if want == 1:
    voltage = float(input("Enter voltage: "))
    resistance = float(input("Enter resistence: "))
    print(amper(voltage, resistance))
elif want == 2:
    amperage = float(input("Enter amperage: "))
    resistance = float(input("Enter resistance: "))
    print(volt(amperage, resistance))
else:
    amperage = float(input("Enter amperage: "))
    voltage = float(input("Enter voltage: "))
    print(om(amperage, voltage))