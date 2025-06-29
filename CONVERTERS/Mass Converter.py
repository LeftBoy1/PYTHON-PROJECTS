print("********** M A S S   C O N V E R T E R **********\n")


mass_units = {
    "kg": 1,
    "g": 0.001,
    "mg": 0.000001,
    "lb": 0.453592,
    "oz": 0.0283495,
    "ton": 1000,       # metric ton (1000 kg)
    "st": 6.35029      # stone
}

print("Available units:")
for unit in mass_units:
    print(f"- {unit}")

from_unit = input("\nEnter the unit to convert FROM (e.g., kg): ").lower()
to_unit = input("Enter the unit to convert TO (e.g., lb): ").lower()

if from_unit not in mass_units or to_unit not in mass_units:
    print("Invalid unit entered. Please try again.")
else:
    value = float(input(f"Enter the value in {from_unit}: "))


    value_in_kg = value * mass_units[from_unit]
    result = value_in_kg / mass_units[to_unit]

    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
