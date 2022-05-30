import datetime

def greeting():
    currentTime = datetime.datetime.now()
    if currentTime.hour < 12:
        print("Good morning")
    elif currentTime.hour < 18:
        print("Good afternoon")
    else:
        print("Good evening")
