print("********** D A T A   C O N V E R T E R **********\n")

# Data units and their equivalent in bytes (base unit)
data_units = {
    "b": 1 / 8,         # bit to byte (1 byte = 8 bits)
    "B": 1,             # byte
    "KB": 1024,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3,
    "TB": 1024 ** 4,
    "PB": 1024 ** 5
}

print("Available units:")
for unit in data_units:
    print(f"- {unit}")

from_unit = input("\nEnter the unit to convert FROM (e.g., MB): ").upper()
to_unit = input("Enter the unit to convert TO (e.g., GB): ").upper()

if from_unit not in data_units or to_unit not in data_units:
    print("Invalid unit entered. Please try again.")
else:
    value = float(input(f"Enter the value in {from_unit}: "))

    # Convert input value to bytes first
    value_in_bytes = value * data_units[from_unit]
    # Convert bytes to target unit
    result = value_in_bytes / data_units[to_unit]

    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
