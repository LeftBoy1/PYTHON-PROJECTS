import datetime
import time
import pygame

target_time = input("Enter time for reminder(eg=> 09:34 AM): ").strip()
x = datetime.datetime.now().strftime("%I:%M %p")

print(f"Current time: {x}\nReminder Set for: {target_time}\nWaiting for Task reminder..." )

while True:
    now = datetime.datetime.now().strftime("%I:%M %p")
    if now == target_time:
        pygame.mixer.init()
        pygame.mixer.music.load("F:\\Devansh Gupta\\Python Basic\\PYTHON PROJECTS\\FREEBEAT.mp3")
        pygame.mixer.music.play()
        print("Reminder: Do your task!")
        
        # ⏳ Wait while music is playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break

    else:
        time.sleep(1)
        
        
        
        
        
        
        
        
        
        
        
        
# USING CHATGPT (adding keyword to stop alarm):
import datetime
import time
import pygame
import threading

# Function to play music
def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("F:\\Devansh Gupta\\Python Basic\\PYTHON PROJECTS\\Michael.mp3")
    pygame.mixer.music.play()

# Function to stop music
def stop_alarm():
    input("Press Enter to stop the alarm...")
    pygame.mixer.music.stop()

target_time = input("Enter time for reminder (e.g., 09:34 AM): ").strip()
target_time = datetime.datetime.strptime(target_time, "%I:%M %p").strftime("%I:%M %p")

print(f"Current time: {datetime.datetime.now().strftime('%I:%M %p')}")
print(f"Reminder set for: {target_time}\nWaiting for Task reminder...")

while True:
    now = datetime.datetime.now().strftime("%I:%M %p")
    if now == target_time:
        print("⏰ Reminder: Do your task!")
        
        play_alarm()

        # Start thread to stop alarm with Enter key
        stop_thread = threading.Thread(target=stop_alarm)
        stop_thread.start()

        # Wait while music is playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)
        break

    time.sleep(1)
