print("********** V O L U M E   C O N V E R T E R **********\n")


volume_units = {
    "l": 1,
    "ml": 0.001,
    "m3": 1000,
    "cm3": 0.001,
    "ft3": 28.3168,
    "in3": 0.0163871,
    "gal": 3.78541,
    "qt": 0.946353,
    "pt": 0.473176
}

print("Available units:")
for unit in volume_units:
    print(f"- {unit}")

from_unit = input("\nEnter the unit to convert FROM (e.g., l): ").lower()
to_unit = input("Enter the unit to convert TO (e.g., gal): ").lower()

if from_unit not in volume_units or to_unit not in volume_units:
    print("Invalid unit entered. Please try again.")
else:
    value = float(input(f"Enter the value in {from_unit}: "))

    
    value_in_liters = value * volume_units[from_unit]
    result = value_in_liters / volume_units[to_unit]

    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
