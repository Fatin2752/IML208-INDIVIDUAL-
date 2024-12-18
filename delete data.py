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
# Function to display appointments
def display_appointments():
    if not appointments:
        print("\nNo appointments available.")
        return
    print("\nCurrent Appointments:")
    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. Name: {appointment['name']}, ID: {appointment['id_number']}, Age: {appointment['age']}, "
            f"Gender: {appointment['gender']}, Date: {appointment['date']}, Time: {appointment['time']}, "
            f"Contact: {appointment['contact']}"
        )
# Function to delete an appointment
def delete_appointment():
    display_appointments()
    if not appointments:
        return
    try:
# Choose an appointment to delete
        choice = int(input("\nEnter the number of the appointment you want to delete: ")) - 1
        if choice < 0 or choice >= len(appointments):
            print("Invalid choice. Please try again.")
            return
# Confirm deletion
        confirmation = input(f"Are you sure you want to delete the appointment for {appointments[choice]['name']}? (yes/no): ").strip().lower()
        if confirmation == "yes":
            deleted_appointment = appointments.pop(choice)
            print(f"\nAppointment for {deleted_appointment['name']} has been deleted.")
        else:
            print("\nDeletion canceled.")
    except ValueError:
        print("Invalid input. Please try again.")
if __name__ == "__main__":
    print("Welcome to the Medical Appointment System!")
    delete_appointment()
    print("\nUpdated Appointments:")
    display_appointments()