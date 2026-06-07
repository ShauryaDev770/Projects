import datetime
import pandas as pd
import matplotlib.pyplot as plt

def time():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d")
    return timestamp

class Finance:

    def __init__(self,data):
        self.data = data
    
    def total_expense(self):
        total = sum(self.data.values())
        return (f"The total expence is: {total}")
    
    def highest_expense(self):
        max_val = max(self.data.values())
        max_key = max(self.data, key=self.data.get)   # I discoverd .get method for finding out the key with max value
        return (f"You spent most on {max_key} with amount {max_val}")


def get_expenses(category):   # Getting expence data for the category
    while True:
        try:
            value = float(input(f"Enter the expense for {category}: ")) 
            if value <0:
                print("Please enter a valid amount")
            else:
                return value
        except ValueError:
            print("Invalid input")


def menu():   #Collecting data
    data = {}
    while True:
        category = input("Enter the category (food, travel, shopping, rent, etc) or enter 'done' to exit: ").lower()
        if category == "done":
            break
        elif category in data:
            choice = input("Category already exists. Do you want to replace the previous one? (y/n)")
            if choice=="y":
                pass
            else:
                continue
        value = get_expenses(category)
      
        data[category]=value
       
    return data



final_data = menu()
finance = Finance(final_data)

finance.total_expense()
finance.highest_expense()

categories = list(final_data.keys())
amount = list(final_data.values())

plt.pie(amount,labels=categories,autopct="%1.2f")
plt.show()

with open("Finance_Tracker.txt","a") as f:
    f.write(str(time()))
    f.write(f"\nThis month expence:\n{final_data}")
    f.write(f"\n{finance.total_expense()}\n")
    f.write(f"\n{finance.highest_expense()} \n")


'''
My Mistakes 
>> I created a loop but forgot to close it with a break syntax.
>> I made a worng funtion for get_expences as i was really confused in how to use the category variable.
>> I created a dictionary but couldn't able to save it and pass onto Finance

'''
'''
point to remmber
>> ValueError in except is used for handling the error when the user enters a value that is not a number

'''

