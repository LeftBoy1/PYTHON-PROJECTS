from plyer import notification
import time

def show_notification():
    notification.notify(
        title = 'Time to Refocus!',
        message = 'Stay productive, Devansh',
        timeout = 5
    )


while True:
    show_notification()
    print("Notification sent. Waiting 30 seconds to send notification again...\n")
    time.sleep(30)  # Wait for 30 seconds before sending next notification
