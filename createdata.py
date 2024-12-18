#medical appointment booking system
#list to store appointment details
appointments = [
    {
        "name" : "Alicia",
        "id_number" : "98261",
        "age" : "25",
        "gender" : "female",
        "date" : "2023-11-6",
        "time" : "10:00 AM",
        "contact" : "182-547-726",
    }
]
#function to book a new appointment
def book_appointment():
    print("\nbooking a new appointment..")
    name = input("enter patient's name:")
    id_number = input("enter patient's id number:")
    age = int(input("enter patient's age:"))
    gender = input("enter patient's gender (male/female):")
    date = input("enter appointment date (YYYY-MM-DD):")
    time = input("enter appointment time (HH:MM AM/PM):")
    contact = input("enter patient's contact number:")
#create a new appointment
appointment = {
    "name" : ["Alicia"],
    "id_number" : ["98261"],
    "age" : ["25"],
    "gender" : ["female"],
    "date" : ["2023-11-6"],
    "time" : ["10:00 AM"],
    "contact" : ["182-547-726"],
}
appointments.append(appointment)
print(f"appointment successfully booked for {"Alicia"} on {"2023-11-6"} at {"10:00 AM"}. ")

#function to display all appointments
def display_appointments ():
    if not appointments:
        print("\nNo aapointments found.")
        return
    print("\nList af all appointments:")
    for index, appointment in enumerate(appointments, start=1 ):
        print(
            f"appointment {index}:"
            f"name: {appointment['name']}, id: {appointment['id_number']}, age: {appointment['age']},"
            f"gender: {appointment['gender']}, date: {appointment['date']}, time: {appointment['time']},"
            f"contact: {appointment['contact']}"
        )