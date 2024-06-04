import time 


def countdown_timer(total_wait_time):
    while total_wait_time > 0:
        print(f"Time remaining: {total_wait_time} seconds", end="\r")
        time.sleep(1)
        total_wait_time -= 1
    if total_wait_time <= 0:
        print("\n")
        wait_time_seconds = int(input('Enter seconds '))
        wait_time_minutes = int(input('Enter minutes '))
        wait_time_hours = int(input('Enter hours '))
        total_wait_time = wait_time_hours*3600 + wait_time_minutes*60 + wait_time_seconds
        

        countdown_timer(total_wait_time)
        
# get the number of seconds to wait from the user 

wait_time_seconds = int(input('Enter seconds '))
wait_time_minutes = int(input('Enter minutes '))
wait_time_hours = int(input('Enter hours '))

total_wait_time = wait_time_hours*3600 + wait_time_minutes*60 + wait_time_seconds
countdown_timer(total_wait_time)
