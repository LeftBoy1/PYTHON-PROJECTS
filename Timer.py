from playsound import playsound
import time

class CountdownTimer:
    def __init__(self, duration):
        self.duration = duration
        self.original = duration  

    def start(self):
        self._countdown(self.duration)

    def _countdown(self, n):
        if n == 0:
            self._play_sound()
            print("It's Over!")
        else:
            if n == self.original // 2:
                print("Half Time!")
            print(n)
            time.sleep(1)
            self._countdown(n - 1)

    def _play_sound(self):
        try:
            playsound("Notification_Sound_Effect.mp3")
        except:
            print("Sound failed to play (check path or install)")


time_input = int(input("Enter the time (in seconds): "))
timer = CountdownTimer(time_input)
timer.start()
