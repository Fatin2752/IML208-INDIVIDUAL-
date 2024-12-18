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
    print("\nCurrent Appointments:")
    for index, appointment in enumerate(appointments, start=1):
        print(
            f"{index}. Name: {appointment['name']}, ID: {appointment['id_number']}, Age: {appointment['age']}, "
            f"Gender: {appointment['gender']}, Date: {appointment['date']}, Time: {appointment['time']}, "
            f"Contact: {appointment['contact']}"
        )
# Function to update an appointment
def update_appointment():
    display_appointments()
    try:
# Choose an appointment to update
        choice = int(input("\nEnter the number of the appointment you want to update: ")) - 1
        if choice < 0 or choice >= len(appointments):
            print("Invalid choice. Please try again.")
            return
# Select which field to update
        field = input("Enter the field you want to update (name, id_number, age, gender, date, time, contact): ").strip().lower()
        if field not in appointments[choice]:
            print("Invalid field. Please try again.")
            return
# Update the chosen field
        new_value = input(f"Enter the new value for {field}: ").strip()
        appointments[choice][field] = new_value
        print("\nAppointment updated successfully!")
    except ValueError:
        print("Invalid input. Please try again.")
if __name__ == "__main__":
    print("Welcome to the Medical Appointment System!")
    update_appointment()
    print("\nUpdated Appointments:")
    display_appointments()