import time
import os
import cv2

# Predefined valid data for checking
valid_countries = ["india", "japan", "america", "canada", "australia"]
valid_states = {
    "india": ["rajasthan", "uttar pradesh", "maharashtra", "gujarat","delhi","andhra pradesh","arunavhal pradesh",],
    "japan": ["tokyo", "osaka", "kyoto"],
    "america": ["california", "texas", "new york"],
    "canada": ["ontario", "quebec"],
    "australia": ["queensland", "victoria"]
}
valid_cities = {
    "rajasthan": ["jaipur", "udaipur","alwar","ajmer"],
    "uttar pradesh": ["lucknow", "kanpur"],
    "maharashtra": ["mumbai", "pune"],
    "gujarat": ["ahmedabad", "surat"],
    "tokyo": ["shinjuku", "shibuya"],
    "california": ["los angeles", "san francisco"],
    "ontario": ["toronto"],
    "queensland": ["brisbane"]
}

def calling(firstname, lastname):
    while True:
        gender = input('Enter your gender "male", "female" or "none": ').lower()
        match gender:
            case "male":
                print("Hello Sir")
                break
            case "female":
                print("Hello Mam")
                break
            case "none":
                print("Hello,", firstname, lastname)
                break
            case _:
                print("Please Enter Valid Gender")

# Get name
while True:
    a = input("Enter your full name: ").strip().lower()
    name_parts = a.split()
    if len(name_parts) >= 2:
        firstname = name_parts[0]
        lastname = name_parts[-1]
        break
    else:
        print("❌ Please enter at least first and last name using SPACE")

calling(firstname, lastname)

# Time and greeting
a = time.localtime().tm_hour
b = time.localtime().tm_min
c = time.localtime().tm_sec

period = "AM" if a < 12 else "PM"
display_hour = 12 if a == 0 else (a - 12 if a > 12 else a)

print(f"The time is {display_hour}:{b}:{c} {period}")
if a < 12:
    print("Good Morning Sir")
elif a <= 16:
    print("Good Afternoon Sir")
else:
    print("Good Night Sir")

def info():
    while True:
        e = input("Enter Your Age: ")
        try:
            e = int(e)
            if 0 < e <= 120:
                break
            else:
                print("❌ Age must be between 1 and 120.")
        except ValueError:
            print("❌ Please enter a valid number for age.")

    while True:
        f = input("Enter your D.O.B (DDMMYYYY): ")
        if f.isdigit() and len(f) == 8:
            f = f[:2] + '/' + f[2:4] + '/' + f[4:]
            break
        else:
            print("Enter Your Valid D.O.B in DDMMYYYY format")

    x = input("Enter Your Hobbies(using ','): ").lower()

    while True:
        g = input("Enter your Phone No.: ")
        if g.isdigit() and len(g) == 10:
            g = int(g)
            break
        else:
            print("Please enter a valid phone number using digits only.")

    while True:
        r = input("Enter your Email Id: ").lower()
        if r.endswith("@gmail.com"):
            break
        else:
            print("❌ Please enter a valid Gmail address (must end with @gmail.com)")

    t = input("Enter your Address: ")

    while True:
        w = input("Enter your Country Name: ").lower()
        if w in valid_countries:
            break
        else:
            print("❌ Invalid country. Try one of:", ", ".join(valid_countries))

    while True:
        p = input("Enter your State Name: ").lower()
        if p in valid_states.get(w, []):
            break
        else:
            print("❌ Invalid state for selected country. Try one of:", ", ".join(valid_states.get(w, [])))

    while True:
        m = input("Enter your City Name: ").lower()
        if m in valid_cities.get(p, []):
            break
        else:
            print("❌ Invalid city for selected state. Try one of:", ", ".join(valid_cities.get(p, [])))

    print("\nYOUR'S-")
    print("      Name: ", "".join(name_parts))
    print("      Age: ", int(e))
    print("      D.O.B: ", f)
    print("      Hobbies: ", x)
    print("      Phone No.:", int(g))
    print("      Email ID: ", r)
    print("      Country Name: ", w)
    print("      State Name: ", p)
    print("      City Name: ", m)
    print("      Address: ", t)

    return e, f, x, g, r, t, w, p, m

# Call info function
e, f, x, g, r, t, w, p, m = info()

def optional():
    while True:
        qw = input("Type 1 to proceed further and Type 2 to Stop: ").lower()
        if qw == "1":
            while True:
                pr = input("ok\nDO you want to see your Beauty Level? ").lower()
                if pr == "yes":
                    ready = input("OK\nNow put your face in front of Camera...\nAre you Ready? ").lower()
                    if ready == "yes":
                        print("Checking....")
                        cap = cv2.VideoCapture(0)
                        if not cap.isOpened():
                            print("❌ Unable to access the camera")
                        else:
                            start_time = time.time()
                            print("Opening 📷Camera")
                            while True:
                                ret, frame = cap.read()
                                if not ret:
                                    print("❌ Failed to grab frame")
                                    break
                                cv2.imshow("Your Camera View", frame)
                                if time.time() - start_time > 5:
                                    break
                                if cv2.waitKey(1) & 0xFF == ord('q'):
                                    break
                            cap.release()
                            cv2.destroyAllWindows()
                        time.sleep(2)
                        print("Let's go\nYOUR BEAUTY LEVEL COMES 100%\nYEAHHHHH!!!!!!!")
                    elif ready == "no":
                        print("But I’ll tell you anyway")
                        print("Checking....")
                        time.sleep(5)
                        print("Soooooooo\nYOUR BEAUTY LEVEL COMES 100%\nYEAHHHHH!!!!!!!")
                    else:
                        print("I’ll take that as a yes 😉\nYOUR BEAUTY LEVEL COMES 100%!")
                    break
                elif pr == "no":
                    print("Ok, I think you are confident, That's Nice😊")
                    break
                else:
                    print("❌ Please type only 'yes' or 'no'.")
            break
        elif qw == "2":
            print("Bye👋")
            break
        else:
            print("❌ Enter only 1 OR 2")

optional()

# Save file
save_path = r"F:\\Devansh Gupta\\Python Basic\\Personal Data"
os.makedirs(save_path, exist_ok=True)
filename = "_".join(name_parts) + ".txt"
full_path = os.path.join(save_path, filename)

with open(full_path, "w") as file:
    file.write(f"\nYOUR'S-\n")
    file.write(f"Name: {' '.join(name_parts)}\n")
    file.write(f"Age: {e}\n")
    file.write(f"D.O.B: {f}\n")
    file.write(f"Hobbies: {x}\n")
    file.write(f"Phone No.: {g}\n")
    file.write(f"Email ID: {r}\n")
    file.write(f"Country Name: {w}\n")
    file.write(f"State Name: {p}\n")
    file.write(f"City Name: {m}\n")
    file.write(f"Address: {t}\n")

print(f"\n✅ Information saved in file: {full_path}")
print("\nInterrogation Is Completed Now.\n")

