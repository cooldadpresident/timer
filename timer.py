import time 

current_time = time.ctime()
print(current_time)

def countdown_timer(seconds):
    while seconds > 0:
        print(f"Time remaining: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print('Konec')

# get the number of seconds to wait from the user 

wait_time_seconds = int(input('Enter seconds '))
wait_time_minutes = int(input('Enter minutes' ))
wait_time_hours = int(input('Enter hours' ))

total_wait_time = wait_time_hours*3600 + wait_time_minutes*60 + wait_time_seconds
countdown_timer(total_wait_time)
