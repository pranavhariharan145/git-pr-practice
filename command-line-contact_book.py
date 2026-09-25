# Command_Line Contact Book

# Helper function to get values using dictionary

def get_values():
    return {
        "serial_number": int(input("Enter Serial Number: ")),
        "firstname": input("Enter First Name: "),
        "lastname": input("Enter Last Name: "),
        "phoneno": input("Enter Phone Number: "),
        "email": input("Enter Email: "),
        "city": input("Enter City: "),
        "state": input("Enter State: "),
        "zip_code": input("Enter Zip Code: ")
    }

# Create new Conatct Book
def create_contact_book(): 
    
    # Storing in Dictionary
    data_dict = get_values()
    
    # Opening with Writing mode Writing the dictionary to the data.txt
    with open('data.txt','w' ,encoding="utf-8") as f:
        keys = [key for key in data_dict.keys()]
        values = [value for value in data_dict.values()]
        for keys in keys:
                    f.write(keys + " ")
        f.write("\n")
        for value in values:
            f.write(str(value) + " ")
        f.write("\n")


# Add Contacts
def add_contacts():
    
    # Storing in Dictionary
    data_dict = get_values()
    
    # Opening with append mode Writing the dictionary to the data.txt
    with open('data.txt','a' ,encoding="utf-8") as f:
        values = [value for value in data_dict.values()]
        for value in values:
            f.write(str(value) + " ")
        f.write("\n")

# Opening with append mode read data.txt
def read_contacts():
    with open('data.txt','r' ,encoding="utf-8") as f:
        first_line = f.read()
        print(first_line)



# Opeations
print("\n\n")
print("----------------------------------")
print("Command_Line Contact Book")
print("----------------------------------")
while True:
    print("\n\n")
    print("Select a Command and Enter Your Choice")
    print("1. Erase and Create New Contacts")
    print("2. Add Contacts")
    print("3. View the Contacts")
    print("4. Exit")

    choice = int(input("Enter your Choice: "))
    if choice == 1:
        print("Enter Contact Details below")
        create_contact_book()
        print("Erased Existing and Created new Conatact Successfully!!!!")     
    if choice == 2:
        print("Enter Contact Details below")
        add_contacts()
        print("Created new Conatact Successfully")  
    if choice == 3:
        read_contacts()
    if choice == 4:
        print("Bye!!")
        break