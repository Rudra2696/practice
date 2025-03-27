import time
import threading

def timer(seconds):
    print(f"Timer started for {seconds} seconds")
    time.sleep(seconds)
    print("Time's up!")


while True:
    try:
        n=int(input("Enter time in form of seconds : "))
        if n>0:
            break
        else:
            print("Please enter a positive number")
    except (ValueError,TypeError,SyntaxError):
        print("Invalid Input")
    

t = threading.Thread(target=timer, args=(n,))
t.start()
