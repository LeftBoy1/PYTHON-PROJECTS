from math import sqrt

while True:
    try:
        a = float(input("Enter The Value: "))    
    except ValueError:
        print(" Invalid number! Please enter a valid numeric value.\n")
        continue

    try:
        b = int(input("\n 1. Square \n 2. Square Root \n => "))
    except ValueError:
        print(" Invalid choice! Please enter '1' or '2' only.\n")
        continue
    
    
    
    
    if b ==1:
        r = a*a
        print(f"Your Square is: {r}")
        
    elif b == 2:
        if a < 0:
            print("❌ Cannot calculate square root of a negative number.\n")
            continue
        t = sqrt(a)
        print(f"Your SquareRoot is: {t}")
        
    else:
        print("Please Enter only '1' or '2'")
        continue
        
    
    
    while True:  
        again = input("Do You Want To Move Further? (y/n) : ").lower()
        if again == "y":
            continue
        elif again == "n":
            exit()
        else:
            print("INVALID !!! \n Please enter 'y' or 'n' only\n")