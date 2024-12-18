#list of patient appointment
appointments = [
    {
        "name" : ["Alicia"],
        "id_number" : ["98261"],
        "age" : [25],
        "gender" : ["female"],
        "date" : ["2023-11-6"],
        "time" : ["10:00 AM"],
        "contact" : ["182-547-726"],
    }
]
#check appointment availibility
appointment_date = input("enter appointment date:")
if appointment_date == "2023-11-6":
    print("this date already full.")
elif appointment_date == "2023-11-10":
    print("this date is available.")
else:
    print("invalid date or date is not available.")

appointment_time = input("enter appointment time:")
if appointment_time == "10:00 AM":
    print("this time slot already booked.")
elif appointment_time == "3:00 PM":
    print("this time slot is availabe.")
else:
    print("invalid time or time is not available.")