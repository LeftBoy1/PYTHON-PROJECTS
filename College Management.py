import os
while True:
    
    while True:
        a = input("Enter Student full name: ").strip().lower().title()
        name_parts = a.split()
        if len(name_parts) >= 2:
            firstname = name_parts[0].capitalize()
            lastname = name_parts[-1].capitalize()
            break
        else:
            print("Please enter at least first and last name using SPACE")

    while True:
        gender = input('Enter your gender ("male", "female", or "none"): ').strip().lower()
        if gender in ['male', 'female', 'none']:
            gender = gender.capitalize()
            break
        else:
            print("Please enter a valid gender")





    b = int(input("Enter Student Roll No.: "))

    c = (input("Enter Student Class and Section: "))

    d = input("Session(using Space'-'): ")


    while True:
        x = input("Enter your Phone No.: ")
        if x.isdigit() and len(x) == 10:
            e = int(x)
            break
        else:
            print("Please enter a valid phone number using digits only.")

    while True:
        f = input("Enter your D.O.B (DDMMYYYY): ")
        if f.isdigit() and len(f) == 8:
            f = f[:2] + '/' + f[2:4] + '/' + f[4:]
            break
        else:
            print("Enter Your Valid D.O.B in DDMMYYYY format")

    while True:
        e = input("Enter Your Age: ")
        try:
            e = int(e)
            if 0 < e <= 120:
                break
            else:
                print("Age must be between 1 and 120.")
        except ValueError:
            print("Please enter a valid number for age.")
            
    while True:
        m = input("Enter your City Name: ").strip().lower()
        if m.replace(" ", "").isalpha():
            city = m.title()
            break
        else:
            print("Please enter a valid City Name.")

                
    while True:
        z = input("Enter your State Name: ").strip().lower()
        if z.replace(" ", "").isalpha():
            state = z.title()
            break
        else:
            print("Please Enter a Valid State Name.")

    def mark(firstname, lastname, b, f, e, gender, c, d, x, city, state):

        r = int(input("Total Marks: "))
        q = int(input("Marks Obtained: "))
        l = (q / r) * 100
        p = l / 10
        
        
        
        print("\n" + "-" * 120)
        print("\n************************************ S  T  U  D  E  N  T     D  E  T  A  I  L  S ***************************************")
        print("=" * 120 + "\n")

        print(f"Student Name: {firstname} {lastname}")
        print(f"Gender: {gender}")
        print("Roll No.:", b)
        print("Age:", e)
        print("D.O.B:", f)
        print("Class & Section:", c)
        print("Session:", d)
        print("Phone No.:", x)
        print("City Name:", city)
        print("State Name:", state)
        
        print("\n" + "-" * 120)
        print("\n*************************************** M  A  R  K  S     D  E  T  A  I  L  S ******************************************")
        print("=" * 120 + "\n")

        
        print("Total Marks: ", r)
        print("Marks Obtained:", q)
        print("Total Percentage:", round(l, 2), "%")
        print("Total CGPA:", round(p, 2))

        return r, q, round(l, 2), round(p, 2)
    r, q, l, p = mark(firstname, lastname, b, f, e, gender, c, d, x, city, state)


    save_path = r"F:\Devansh Gupta\Python Basic & ADVANCED\PYTHON PROJECTS"             
    os.makedirs(save_path, exist_ok=True)
    filename = "_".join(name_parts) + ".txt"
    full_path = os.path.join(save_path, filename)

    with open(full_path, "w") as file:
        
        file.write("\n" + "-" * 120)
        file.write("\n************************************ S  T  U  D  E  N  T     D  E  T  A  I  L  S ***************************************\n")
        file.write("=" * 120 + "\n")
        file.write(f"Student Name: {' '.join(name_parts)}\n")
        file.write(f"Gender: {gender}\n")
        file.write(f"Roll No.: {b}\n")
        file.write(f"Age: {e}\n")
        file.write(f"D.O.B: {f}\n")
        file.write(f"Class & Section: {c}\n")
        file.write(f"Session: {d}\n")
        file.write(f"Phone No.: {x}\n")
        file.write(f"City Name: {city}\n")
        file.write(f"State Name: {state}\n")
        file.write("\n" + "-" * 120)
        file.write("\n*************************************** M  A  R  K  S     D  E  T  A  I  L  S ******************************************\n")
        file.write("=" * 120 + "\n")
        file.write(f"Total Marks: {r}\n")
        file.write(f"Marks Obtained: {q}\n")
        file.write(f"Total Percentage: {l}\n")
        file.write(f"Total CGPA: {p}\n")

    print(f"\n✅ Information saved in file: {full_path}")


    t = input("\nDo you want to enter another student's details? (y/n): ")
    if t!="y":
        break

