import json
import os
import requests

def file_management():
    if os.path.exists('library.json') and os.path.getsize('library.json')>0:
        with open("library.json","r") as f:
            return json.load(f)
    return []

def save_new_books(books_stored):
    with open('library.json',"w") as file:
        json.dump(books_stored,file,indent=4)


class Library:
    def add_books(self):
        while True:   
            book = input("Please enter the book name: ")
            url = "https://openlibrary.org/search.json"
            params = {"q" : book} 
            try:
                response = requests.get(url,params = params)
            except requests.exceptions.Timeout:
                print("Request timed out. Try again")
                return
            except requests.exceptions.RequestException as e:
                print("Network error: ",e)
                return
            
            data = response.json()

            info = {
            'Title' : data['docs'][0]["title"],
            'Author name' : data['docs'][0]["author_name"],
            'First Published Year' : data['docs'][0]['first_publish_year']
            }

            existing = file_management()

            existing.append(info)

            save_new_books(existing)
            choice = input("Do you want to add more books? (y/n) ")
            if choice == "n":
                break
            else:
                continue
    
    def remove_book(self):
        while True:
            book_removal = input("Name the book you want to remove: ")
            data = file_management()
            found = False
            for book in data:
                if book['Title'] == book_removal:
                   data.remove(book)
                   found =True
                   print("Book Removed")
                
                if not found:
                    print("Book not found")
            
            save_new_books(data)

            choice = input("Do you want to remove more books? (y/n) ")
            if choice == "n":
                break
            else:
                continue

# Terminal UI
call = Library()

print("----------------------Books in the library-----------------------")

Title = file_management()
if Title ==0:
    print("No book in the library")
else:
    for i in Title:
        print(i)


while True:
    ask = input("What do you want to do? [Add a book,Delete a book]>> (Add/Delete/exit): ").lower()

    if ask == "add":
        call.add_books()
        
    elif ask == 'delete':
        call.remove_book()
       
    elif ask == 'exit':
        break

    else:
        print('Please Specify')
        continue



    








'''
Mistakes I made!
>> Forgot to save the file before running it.
'''
    
