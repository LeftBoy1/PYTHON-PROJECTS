from playsound import playsound

def countdown(n):
    if n == 0:
        playsound("BLAST.mp3")
        print("Blast🔥!!!")
    else:
        playsound("Beep.mp3")
        print(n)
        countdown(n - 1)

Number = int(input("Enter the no. to start Countdown: "))
countdown(Number)
