import pandas as pd
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
        for item_unit in valid_ans:
            if response == item_unit:
                return item_unit
        # if the user inputs <blank> then the program will
        # presume the user wants each
        if response == "":
            return "ea"
        else:
            print("error")

def unit_converter(item_weight, item_unit):
    """convert grams or ml to kg and l"""
    if item_unit in ["ml", "g"]:
        item_weight = item_weight / 1000
    return item_weight

def price_calculator(unit_price, item_weight):
    """work out the unit price"""
    per_kg_l = unit_price / item_weight
    # round the price per kg/l to 2dp
    rounded = round(per_kg_l, 2)
    return rounded

def recommendation(df, budget_1, type_1="cheapest"):
    # under budget area
    affordability = df[df["Cost"] <= budget_1]

    # cheapest unit area
    recommendation_0 = df.sort_values(by="Unit cost")
    cheapest_unit = recommendation_0.iloc[[0]]

    if type_1 == "affordability":
        if affordability.empty:
            return "There are no items under your budget."

        affordability_1 = affordability.sort_values(by="Cost")
        list_1 = affordability_1.iloc[[0]]

    else:
        list_1 = cheapest_unit

    lookup_name = list_1.iloc[0, 0]
    lookup_weight = list_1.iloc[0, 1]
    lookup_cost = list_1.iloc[0, 2]
    lookup_unit = list_1.iloc[0, 3]
    lookup_unit_cost = list_1.iloc[0, 4]

    # return area
    if type_1 == "affordability":
        output = (f"{lookup_name} is the cheapest item under your budget at ${lookup_cost} "
                f"for {lookup_weight} {lookup_unit} with a unit cost of ${lookup_unit_cost} per {lookup_unit}.")
    elif type_1 == "cheapest":
        output = (f"{lookup_name} has the lowest unit cost in your comparison at ${lookup_cost} "
          f"for {lookup_weight} {lookup_unit} with a unit cost of ${lookup_unit_cost} per {lookup_unit}.")
    else:
        output = "Error"

    return output
# main routine starts here

# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []
all_item_per_kg = []

item_count = 0
# this is the dictionary
price_comparison_dict = {
    'Name': all_item_name,
    'Weight': all_item_weight,
    'Cost': all_item_cost,
    'Unit': all_item_unit,
    'Unit cost': all_item_per_kg
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

    # when called the function works changes g / mL to KG / L
    unit_converter_1 = unit_converter(weight, unit_question)
    # calculate the price per unit
    price_cal = price_calculator(item_cost, unit_converter_1)

    # add item name, item weight, item cost and unit
    all_item_name.append(item_name)
    all_item_weight.append(weight)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_question)
    all_item_per_kg.append(price_cal)
    item_count += 1

if item_count > 1:
    recommendation_frame = pd.DataFrame(price_comparison_dict)

    recommendation_string = tabulate(recommendation_frame, headers='keys',
                                     tablefmt='psql', showindex=False, numalign="right")
    print(recommendation_string, "hello")
    recommendation_affordability = recommendation(recommendation_frame, budget, "affordability")
    print(recommendation_affordability)
    recommendation_lowest_unit = recommendation(recommendation_frame, budget)
    print(recommendation_lowest_unit)


    name = input("What would you like the file name to be? ")
    if name == "":
        name = "Price_comparison"
    print("Good Bye have a bad day🤣🤣🤣")





    to_write = []
    # print area
    print()
    for item in to_write:
        print(item)

    # create file to hold data (add .txt extension)
    file_name = f"{name}_{year}_{month}_{day}"
    write_to = "{}.txt".format(file_name)

    text_file = open(write_to, "w+")

    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

else:
    print("Sorry you didn't enter anything")