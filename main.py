# I want to find amperage

print("You want know amperage, voltage or resistance")
voltage = float(input("Enter voltage: "))
om = float(input("Enter om: "))

def amperage(voltage, om):
    amper = voltage / om
    return str(amper)

print("Amperage = " + amperage(voltage, om))