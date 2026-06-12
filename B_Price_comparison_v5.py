import pandas
from datetime import date
from tabulate import tabulate

# functions goes here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)
        # checks if the user entered something that is NOT blank
        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def yes_no(question):
    """Checks that users entered yes / y or no / n to a question"""

    while True:
        response = input(question).lower()
        # checks if the user entered yes / y for yes
        if response == "yes" or response == "y":
            return "yes"
        # checks if the user entered no / n for no
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def instructions():
    """Prints the instructions"""
    make_statement("Heading", "💰")

    print('''
Instructions 
    ''')

def num_check(question):
    """checks that the input the user entered is a number more than 0"""
    while True:
        response = input(question).lower()
        try:
            response = float(response)
            # checks if the user response is greater then 0
            if response > 0:
                return response
            else:
                error = "Please enter a positive number"
                print(error)
        except ValueError:
            print("Please enter numbers (Not Letters!)")

def unit(question, valid_ans=("ml", "l", "g", "kg", "ea")):
    """Takes the user answer and checks if it's a valid answer from the list!"""
    while True:
        response = input(question).lower()
        # checks if the item is in the list
        for item in valid_ans:
            if response == item:
                return item
        # if the user inputs <blank> then the program will
        # presume the user wants each
        if response == "":
            return "ea"
        else:
            print("error")

def unit_price_calculator(item_weight, items_unit, unit_price):
    """convert units and also works out the price per unit"""
    if items_unit == "ml" or items_unit == "g":
        print("you are in the ml / g loop")
        item_weight = item_weight / 1000

    per_kg_l = unit_price / item_weight
    return per_kg_l
# main routine starts here

# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []
all_item_per_kg = []
# this is the dictionary
price_comparison_dict = {
    'Name': all_item_name,
    'Weight': all_item_weight,
    'Cost': all_item_cost,
    'Unit': all_item_unit,
    'per_unit': all_item_per_kg
}
# instructions
want_instructions = yes_no("Do you want to see the instructions? ")
if want_instructions == "yes":
    instructions()

# for file names
# **** Get current date for heading and file name ****
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")
# gets the users budget
budget = num_check("What is your budget? ")

while True:
    # gets the details of the items
    item_name = not_blank("What is the item name? ")
    if item_name == "xxx":
        break
    weight = num_check("What is the weight? ")
    unit_question = unit("what is the unit? ")
    item_cost = num_check("What is the item cost? ")

    # when called the function works changes g / mL to KG / L and then
    # works out the price per kg / l / ea
    unit_test = unit_price_calculator(weight, unit_question, item_cost)
    # add item name, item weight, item cost and unit
    all_item_name.append(item_name)
    all_item_weight.append(weight)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_question)
    all_item_per_kg.append(unit_test)
print("Good Bye have a bad day🤣🤣🤣")