import time
import threading

def timer(seconds):
    print(f"Timer started for {seconds} seconds")
    time.sleep(seconds)
    print("Time's up!")

# Start the timer without blocking other code
t = threading.Thread(target=timer, args=(5,))
t.start()
