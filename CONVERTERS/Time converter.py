print("********** T I M E   C O N V E R T E R **********\n")

time_units = {
    "s": 1,
    "min": 60,
    "h": 3600,
    "day": 86400,
    "week": 604800,
    "month": 2629800,   # average month in seconds (30.44 days)
    "year": 31557600    # average year in seconds (365.25 days)
}

print("Available units:")
for unit in time_units:
    print(f"- {unit}")

from_unit = input("\nEnter the unit to convert FROM (e.g., min): ").lower()
to_unit = input("Enter the unit to convert TO (e.g., h): ").lower()

if from_unit not in time_units or to_unit not in time_units:
    print("Invalid unit entered. Please try again.")
else:
    value = float(input(f"Enter the value in {from_unit}: "))


    value_in_seconds = value * time_units[from_unit]

    result = value_in_seconds / time_units[to_unit]

    print(f"\n{value} {from_unit} = {result:.4f} {to_unit}")
