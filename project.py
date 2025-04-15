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