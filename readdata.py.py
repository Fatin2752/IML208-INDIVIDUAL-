#function to display all appointments
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
def read_appointments():
    print("\nMedical Appointment Data:")
    for appointment in appointments:
        print(f"Name : {appointment['name']}")
        print(f"ID : {appointment['id_number']}")
        print(f"Age : {appointment['age']}")
        print(f"Gender : {appointment['gender']}")
        print(f"Date : {appointment['date']}")
        print(f"Time : {appointment['time']}")
        print(f"Contact : {appointment['contact']}")
        print("-" * 40)
read_appointments ()