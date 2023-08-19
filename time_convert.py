def time_convert(timeStr):
    splitTime = timeStr.split(" ")
    splitRealTime = splitTime[0].split(":")
    toInt = int(splitRealTime[0])
    
    if splitTime[1] == "am" and toInt == 12:
        formatted_time = "00" + ":" + splitRealTime[1]
    elif splitTime[1] == "pm" and toInt < 12:
        toInt += 12
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
    else:
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
        
    print(formatted_time)    
    return formatted_time

# time_convert("12:30 am")





# time_convert("3:30 pm")
time_convert("2:30 am")