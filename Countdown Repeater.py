import time
while True:
    try:
        
        try:
            t = int(input("How many times do you want to repeat?: "))
            n = int(input("Enter the number to count up to: "))
            print(f"\nYou asked Repeating for {t} times and counting starts from {n}.")
            print("\nSTARTING\n")
            for _ in range(t):
                for i in range (1,n+1):
                    print(i)
                    time.sleep(1)
                print("_")
            break
        except ValueError:
            print("Please enter valid no.")   
            
    except ValueError:
        print("Please enter valid no.")
        