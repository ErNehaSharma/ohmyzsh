import time

def countdown_timer(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        seconds -= 1

    print("Time's up!")

if __name__ == "__main__":
    try:
        seconds = int(input("Enter the number of seconds to countdown: "))
        countdown_timer(seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
