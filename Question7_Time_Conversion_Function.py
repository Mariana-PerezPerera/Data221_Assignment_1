#time conversion function
#write a function that converts a given number of seconds since midnight into
#creating the function that is taking in seconds since midnight:
def convertion_of_seconds_since_midnight(seconds_since_midnight):
    if (not isinstance(seconds_since_midnight, int) or
            seconds_since_midnight < 0 or
            seconds_since_midnight >= 86400):
            return "Invalid input."

#assigning the variables and calculating them:
    hours = seconds_since_midnight // 3600
    minutes = (seconds_since_midnight % 3600) // 60
    seconds = seconds_since_midnight % 60

#assinging the time period:
    time_period = "AM" if hours < 12 else "PM"

    hours = hours % 12
    if hours == 0:
        hours = 12

    return f"{hours} {minutes} {seconds} {time_period}"


#printing the final conversion:
print(convertion_of_seconds_since_midnight(22453))


