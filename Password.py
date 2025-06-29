from playsound import playsound 
import time

print("\n This message will destroy in 3 seconds \n")
def countdown(n):
    if n == 0:
        # playsound("BLAST.mp3")
        time.sleep(0.1) 
        playsound("BLAST.mp3")
        print("Blast🔥!!!")
    else:
        # playsound("BEEP.mp3")
        time.sleep(0.1) 
        playsound("Beep.mp3")   
        print(n)
        countdown(n - 1)



def Pass():
    password = "ybhub"
    hints = ["Hint 1: It's a HUB"
             ,"Hint 2: A video on YOUTUBE",
            "Hint 3: bASEBALL"]
    
    for attempt in range(3):
        
        print(hints[attempt])
        x = input("Enter password: ")
        
        if x == password:
            print("Access Granted.✅\n\n                  W E L C O M E  T O  T H E  W O R L D ! ! ! \n\n")
            return  # Exit the function after success
        
        else:
            # time.sleep(0.1) 
            # playsound("wrong.mp3")
            print(f"Incorrect❌! You Have {2 - attempt} Chances Left.\n")
            # print("Incorrect! You Have",2-attempt,"Chances Left.\n")
            
    print("Access Not Granted.👎 Too many wrong attempts.")
    print("\n\n                                         SYSTEM WILL EXPLODE💣 AFTER 10 SECONDS!!!!!!\n\n")
    
    countdown(10)
    

Pass()