def time_convert():
    # Ask the user to provide a time in the format 'hh:mm am/pm'
    timeStr = input("Enter the time in the format 'hh:mm am/pm': ")
    
    # Split the input into two parts: the time and the am/pm indicator
    splitTime = timeStr.split(" ")
    
    # Split the time part further to extract hours and minutes
    splitRealTime = splitTime[0].split(":")
    
    # Convert the hours part to an integer for further processing
    toInt = int(splitRealTime[0])
    
    # Check different cases to handle time conversions
    if splitTime[1] == "am" and toInt == 12:
        # Convert 12:00 am to 24-hour format as 00:00
        formatted_time = "00" + ":" + splitRealTime[1]
    elif splitTime[1] == "pm" and toInt < 12:
        # Convert afternoon times to 24-hour format by adding 12 hours
        toInt += 12
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
    else:
        # Keep times in 24-hour format unchanged
        formatted_time = str(toInt).zfill(2) + ":" + splitRealTime[1]
        
    # Display the converted time to the user
    print(f"Converted time: {formatted_time}")
    return formatted_time

# Call the time_convert function to initiate the time conversion
time_convert()
