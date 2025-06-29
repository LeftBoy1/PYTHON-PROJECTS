print("********** S P E E D   C O N V E R T E R **********\n")


speed_units = {
    "m/s": 1,
    "km/h": 1000 / 3600,
    "mph": 1609.34 / 3600,
    "km/s": 1000,
    "in/s": 0.0254,
    "in/h": 0.0254 / 3600,
    "ft/s": 0.3048,
    "ft/h": 0.3048 / 3600,
    "mi/s": 1609.34,
    "mi/h": 1609.34 / 3600,
    "knots": 1852 / 3600,
    "mach": 343  
}

print("Available units:")
for unit in speed_units:
    print(f"- {unit}")


a = input("\nEnter the unit to convert FROM (e.g., km/h): ").lower()
b = input("Enter the unit to convert TO (e.g., mph): ").lower()

if a not in speed_units or b not in speed_units:
    print("Invalid unit entered. Please try again.")
else:
    value = float(input(f"Enter the value in {a}: "))
    
    value_in_mps = value * speed_units[a]
    result = value_in_mps / speed_units[b]
    
    print(f"\n{value} {a} = {result:.4f} {b}")
