import re

def add_time(start, duration, weekday=None):
	'''
	Takes in start time "H:M AM/PM" and duration "H:M" and an optional weekday string and returns the start time + duration, including how many days later and the day of the week.
	'''
	
	day = 0
	weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

	start_split = re.split(":|\s", start)
	duration_split = re.split(":", duration)

	hour = int(start_split[0])
	minute = int(start_split[1])
	qualifier = start_split[2]

	duration_hours = int(duration_split[0])
	duration_minutes = int(duration_split[1])

	new_hour = hour + duration_hours
	new_minute = minute + duration_minutes

	if qualifier == "PM":  # converts to 24h
		new_hour += 12

	if  new_minute >= 60:  # converts minutes to hours
		new_hour += int(new_minute / 60)
		new_minute = new_minute % 60 

	if new_hour >= 24:  # converts hours to days
		day = int(new_hour / 24)
		new_hour = new_hour % 24
	
	if new_hour < 12:  # converts 24h back to 12h
		new_qualifier = "AM"
	elif new_hour == 12:
		new_qualifier = "PM"
	elif new_hour < 24:
		new_qualifier = "PM"
		new_hour = new_hour % 12

	if new_hour == 0:  # corrects first hour to 12
		new_hour = 12

	new_hour = str(new_hour)
	if new_minute < 10:  # adds 0 to low minute values
		new_minute = "".join("0" + str(new_minute))
	else:
		new_minute = str(new_minute)
	
	new_time = "".join(  # concatenates time string
		new_hour 
		+ ":" 
		+ new_minute
		+ " " 
		+ new_qualifier
	)

	if weekday:  # handles weekdays
		weekday = weekday.capitalize()
		index = weekdays.index(weekday)
		if day > 0:
			index += day
		if index > 6:
			index = index % 7
		new_weekday = weekdays[index]		
		new_time = "".join(new_time + ", " + new_weekday)
		

	if day > 0:  # adds "x days later"
		if day == 1:
			new_time = "".join(new_time + " (next day)")
		else:
			new_time = "".join(new_time + " (" + str(day) + " days later)")

	return new_time