print("********** L E N G T H   C O N V E R T E R **********\n")

# Length units and their equivalent in meters (base unit)
length_units = {
    "m": 1,
    "km": 1000,
    "cm": 0.01,
    "mm": 0.001,
    "mi": 1609.34,
    "yd": 0.9144,
    "ft": 0.3048,
    "in": 0.0254
}

print("Available units:")
for unit in length_units:
    print(f"- {unit}")

from_unit = input("\nEnter the unit to convert FROM (e.g., m): ").lower()
to_unit = input("Enter the unit to convert TO (e.g., ft): ").lower()

if from_unit not in length_units or to_unit not in length_units:
    print("Invalid unit entered. Please try again.")
