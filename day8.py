scanner = str(input("Enter the time in 12-hour format: "))
# Example of input "12:00 PM"
parts = scanner.split(" ")


if len(parts) != 2:
    print("Please Use the format: HH:MM AM/PM")
    exit()


time = parts[0]
period = parts[1].upper()
timepart = time.split(":")

if len(timepart) != 2:
    print("Invalid input")
    exit()

hour = int(timepart[0])
minute = int(timepart[1])

if period == "AM":
    if hour == 12:
        hour = 0
elif period == "PM":
    if hour != 12:
        hour = hour + 12
else:
    print("Invalid period. Use AM or PM.")
    exit()

if hour >= 0 and hour < 12:
    print("Good Morning")
else:
    print("Good Day!")



