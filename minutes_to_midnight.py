
def minutes_to_midnight(hours,minutes, AMPM):
    totalMinutesInADay = 24*60
    
    if AMPM=="PM":
        totalMinutes = 60*hours + minutes+totalMinutesInADay/2
    else:
        totalMinutes = 60*hours + minutes
    
    minutesToMidnight = totalMinutesInADay-totalMinutes
    print("There are ",minutesToMidnight,"till midnight")

def main():
    minutes_to_midnight(5,18,"AM")

if __name__ == "__main__":
    main()

     
    