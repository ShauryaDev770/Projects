import json
import os

def Check_json_file():
    if os.path.exists("Contact.json") and os.path.getsize("Contact.json") > 0:
        with open("Contact.json","r") as json_file:
            return json.load(json_file)
    return {}

def save_changes(data):
    with open("Contact.json", "w") as f:
        json.dump(data, f, indent = 4)

class Contact:

    def Add_Contact(self):  
        new_entry ={}
        while True:
            name = input("Enter the contact name: ").lower()
        
            try: 
                number = str(input("enter the number: "))
                if len(str(number)) != 10:
                    print("Enter a valid 10-digit number")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            new_entry.update({name : number}) 

            more = input("Do you want to add more contacts? (y/n): ").lower()
            if more=="y":
                continue
            else:
                break        

        data = Check_json_file()
        data.update(new_entry)

        save_changes(data)

        print("Contact added successfully!")
    

    def view_contacts(self):
        data = Check_json_file()

        if data == {}:
            print("No contacts are saved.")
        else:
            print(data)
        

    def search_contact(self):
        while True:
            data = Check_json_file()
            search = input("Enter the contact name you want to search:").lower()
            
            if data.get(search) == None:
                print(f"No contacts are saved as '{search}'")
            else:
                print(data.get(search))

            ask = input("Do you want to search more contacts? (y/n): ").lower()
            if ask == "y":
                continue
            else:
                break

    
    def delete_contact(self):
        while True:
            data= Check_json_file()
            delete = input("Enter the contact name you want to delete:").lower()

            if data.get(delete) == None:
                print("The Contact name does not exist.")
                continue
            else:
                del data[delete]
                print("Contact deleted successfully!")
                
                save_changes(data)

            ask = input("Do you want to delete more contacts? (y/n): ").lower()
            if ask == "y":
                continue
            else:
                break
    
    def update(self):
        while True:
            data =Check_json_file()
            update_name = input("Enter the contact name you want to update: ").lower()
    
            if data.get(update_name) == None:
                print("The Contact name does not exist.")
            else:   
                new_number = int(input("Enter the new contact number: "))
                data.update({update_name : new_number})
                print("Contact updated successfully!")
                save_changes(data)

            ask = input("Do you want to update more contacts? (y/n): ").lower()
            if ask == "y":
                continue
            else:
                break
         
contact = Contact()

print("\n-------------------------------- Welcome to the Contact Management System --------------------------------\n")

while True:
    Choice = input("\nWhat do you want to do? (Add/View/Search/Delete/Update/exit): ").lower()

    if Choice == "add":
        contact.Add_Contact()

    elif Choice == "view":
        contact.view_contacts()

    elif Choice == "search":
        contact.search_contact()
    
    elif Choice == "delete":
        contact.delete_contact()
    
    elif Choice == "update":
        contact.update()
    
    elif Choice == "exit":
        print("\n-------------------------------- Thanks for using the Contact Management System --------------------------------\n")
        break
    
    else:
        print("Please Specify")
        continue
    
'''
Mistakes I made!
>> The firat mistake was in reading the length of an integer using len() function but it is only possible for 
a string not for an integer. 

>> The second mistake was that i was bad fromating as i was accidently took file handleing code outside of
Add_contact() funtion.

>> The third mistake was using append function in a dictionary which is not possible as dict only use update
function.

>> While defining the delete function, i deleted the key but didn't realise that we also have to save the updated dictionary to the json file.

'''

'''
Things I learned!

>> I learned the use of os.path.exists() and os.path.getsize() functions.

>> I leanred the structure of how to first read a json file, then update it and then write it back to the file.

>> Without self, it acts more like a standalone utility function, with self, it is an instance method.
'''







    
    

