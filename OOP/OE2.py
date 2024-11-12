class Phone:
    def __init__(self, brand):
        self.brand = brand
        
def display_menu():
    print("\nMenu:")
    print("1. See list")
    print("2. Update list")
    print("3. Delete")
    print("4. Exit")
    
def display_phones(phoneArray):
    print("This is your phones: ")
    for phones in phoneArray:
        print(phones.brand)

def update_phone(phoneArray):
    display_phones(phoneArray) 
    phone_number = int(input("Enter the phone number you want to update: ")) - 1
    if phone_number < len(phoneArray):
        new_brand = input("Enter the new phone brand: ")
        phoneArray[phone_number].brand = new_brand
    else:
        print("Invalid phone number.")
        
def delete_phone(phoneArray):
    display_phones(phoneArray)
    phone_number = int(input("Enter the phone number you want to delete: ")) - 1
    if phone_number < len(phoneArray):
        del phoneArray[phone_number]
    else:
        print("Invalid phone number.")
        
        
quantity = int(input("Enter how many phones you will put: "))

phoneArray = []

for phones in range(quantity): 
    userPhone = Phone(input("Enter your phone brand: "))
    phoneArray.append(userPhone)

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        display_phones(phoneArray)
    elif choice == "2":
        update_phone(phoneArray)
    elif choice == "3":
        delete_phone(phoneArray)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")


