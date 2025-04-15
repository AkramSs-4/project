#COMPUTER LAB MANAGEMENT SYSTEM
computer_labs = {
    "Lab 1": {
        "capacity": 20,
        "admin": "Kabuye Hisham",
        "computers": [],
        "schedule": []
    },
    "Lab 2": {
        "capacity": 25,
        "admin": "Ssenoga Akram",
        "computers": [],
        "schedule": []
    },
    "Lab 3": {
        "capacity": 30,
        "admin": "Bushirah Zaid",
        "computers": [],
        "schedule": []
    },
    "Lab 4": {
        "capacity": 34,
        "admin": "Walusimbi Adam",
        "computers": [],
        "schedule": []
    }
}
def add_computers():
    computer_brands = ["Dell", "HP", "Lenovo", "Asus", "Acer"]
    
    for lab_name in computer_labs:
        lab = computer_labs[lab_name]
        for i in range(1, lab["capacity"] + 1):
            brand = computer_brands[i% len(computer_brands)]
            
            if brand == "Dell":
                ram = "8GB"
                storage = "500GB HDD"
                os = "Windows 10"
                processor = "i5"
            elif brand == "HP":
                ram = "16GB"
                storage = "550GB HDD"
                os = "Windows 11"
                processor = "i7"
            elif brand == "Lenovo":
                ram = "8GB"
                storage = "256GB"
                os = "Windows 11"
                processor = "i5"
            elif brand == "Asus":
                ram = "16GB"
                storage = "512GB"
                os = "Windows 11"
                processor = "i6"
            else:  
                ram = "4GB"
                storage = "500GB HDD"
                os = "Windows 10"
                processor = "i3"
            
            lab["computers"].append({
                "number": f"{lab_name}-PC{i:03d}",
                "brand": brand,
                "specs": {
                    "RAM": ram,
                    "Storage": storage,
                    "OS": os,
                    "Processor": processor
                },
                "condition": "Good" if i % 5 != 0 else "Fair"
            })
    
def add_schedules():
    computer_labs["Lab 1"]["schedule"].append({
        "day": "Monday",
        "lesson": "Programming",
        "time": "9:00 AM - 10:00 AM",
        "instructor": "MR. Walusimbi"
    })
    
    computer_labs["Lab 2"]["schedule"].append({
        "day": "Tuesday",
        "lesson": "Networking",
        "time": "10:30 AM - 12:30 PM",
        "instructor": "Mr. Asad"
    })
    
    computer_labs["Lab 3"]["schedule"].append({
        "day": "Wednesday",
        "lesson": "Statistics",
        "time": "8:00 PM - 10:00 PM",
        "instructor": "Mrs. Aisha"
    })
    
    computer_labs["Lab 4"]["schedule"].append({
        "day": "Thursday",
        "lesson": "Maintenance",
        "time": "2:00 PM - 4:00 PM",
        "instructor": "Mr. Asad"
    })

def show_all_labs():
    print("\nAll Computer Labs:")
    for lab_name in computer_labs:
        lab = computer_labs[lab_name]
        print(f"\n{lab_name}:")
        print(f'-Capacity: {lab['capacity']} computers')
        print(f'-Admin: {lab['admin']}')
        print(f'-Computers registered: {len(lab['computers'])}')
        print(f'-Scheduled classes: {len(lab['schedule'])}')

def show_lab_computer(lab_name):
    if lab_name not in computer_labs:
        print("Lab Not Found⛔. Please choose Lab 1, 2, 3, or 4.")
        return
    
    lab = computer_labs[lab_name]
    print(f"\n{lab_name} Schedule:")
    
    if not lab["schedule"]:
        print("No scheduled classes for this lab.")
    else:
        for class_information in lab["schedule"]:
            print(f"\n-Day: {class_information['day']}")
            print(f"-Activity: {class_information['activity']}")
            print(f"-Time: {class_information['time']}")
            print(f"-Instructor: {class_information['instructor']}")

def main_menu():
    add_computers()  
    add_schedules() 

    print("**Computer Lab Management System**")
    
    while True:
        print("\nMain Menu:")
        print("1. View all labs")
        print("2. View computers in a lab")
        print("3. View schedule for a lab")
        print("4. Exit")
        
        choice = input("Please choose an option (1-4): ")
        
        if choice == "1":
            show_all_labs()
        elif choice == "2":
            lab = input("Which lab? (1, 2, 3, or 4): ")
        elif choice == "3":
            lab = input("Which lab? (1, 2, 3, or 4): ")
            show_lab_computer(f"Lab {lab}")
        elif choice == "4":
            print("Exiting Program!!!!!!!!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main_menu()