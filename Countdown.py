from playsound import playsound

def countdown(n):
    if n == 0:
        print("Countdown Over!!")
    else:
        playsound("Beep.mp3")
        print(n)
        countdown(n - 1)

Number = int(input("Enter the time(in sec.) to start Countdown: "))
countdown(Number)
