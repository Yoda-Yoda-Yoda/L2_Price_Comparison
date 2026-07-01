import pandas as pd
from datetime import date
from tabulate import tabulate

# functions goes here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

def not_blank(question):
    """Checks that a user input isn't blank"""
    while True:
        response = input(question)
        # checks if the user entered something that is NOT blank
        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def string_check(question, valid_ans=("yes","no"), string_type=None):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        response = input(question).lower()

        for item1 in valid_ans:
            # check if the user response is a word in the list
            if item1 == response:
                return item1

            # check if the user response it the same as
            # the first letter of an item in the list
            elif response == item1[0]:
                return item1

        if string_type == "unit":
            if response == "":
                return "ea"
        # print error if user doesn't enter something that's valid
        print(error)
        print()

def instructions():
    """Prints the instructions"""
    make_statement("Heading", "💰")

    print('''
Instructions 
    ''')

def num_check(question, min_number=0):
    """checks that the input the user entered is a number more than 0"""
    while True:
        response = input(question).lower()
        try:
            response = float(response)
            # checks if the user response is greater then 0
            if response > min_number:
                return response
            # if the response is under 0 the program will return an error
            else:
                error = f"Please enter a number that is above {min_number}"
                print(error)
        except ValueError:
            print("Please enter numbers (Not Letters!)")

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
    """Works out the best item for the user and gives a recommendation"""
    # checks if empty
    if df.empty:
        return "There are no items in the list"

    # under budget area
    affordability = df[df["Cost"] <= budget_1]

    # cheapest unit area
    recommendation_0 = df.sort_values(by="Unit cost")
    cheapest_unit = recommendation_0.iloc[[0]]

    # checks the type_1 to see what it is wanting and then assigning the table to look up from
    # to list_1
    if type_1 == "affordability":
        if affordability.empty:
            return "There are no items under your budget."

        affordability_1 = affordability.sort_values(by="Cost")
        item_list = affordability_1.iloc[[0]]

    else:
        item_list = cheapest_unit
    # looking up the item in this cell with list_1 being a placeholder for the if statements above
    lookup_name = item_list.iloc[0, 0]
    lookup_weight = item_list.iloc[0, 1]
    lookup_cost = item_list.iloc[0, 2]
    lookup_unit = item_list.iloc[0, 3]
    lookup_unit_cost = item_list.iloc[0, 4]

    # return area for the most affordable item
    if type_1 == "affordability":
        output = (f"{lookup_name} is the cheapest item under your budget at ${lookup_cost} "
                f"for {lookup_weight} {lookup_unit} with a unit cost of ${lookup_unit_cost} per {lookup_unit}.")
    # return area for cheapest item
    elif type_1 == "cheapest":
        output = (f"{lookup_name} has the lowest unit cost in your comparison at ${lookup_cost} "
                f"for {lookup_weight} {lookup_unit} with a unit cost of ${lookup_unit_cost} per {lookup_unit}.")
    else:
        output = "Sorry there was no items in any tables for comparison"

    return output

# main routine starts here

# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []
all_item_per_kg = []
# item count
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
want_instructions = string_check("Do you want to see the instructions? ")
print(want_instructions)
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
budget = num_check("What is your budget (Minimum budget of more than 20)? ", 20)

while True:
    # gets the details of the items
    item_name = not_blank("What is the item name? ")
    if item_name == "xxx":
        break
    weight = num_check("What is the weight? ")
    unit_question = string_check("what is the unit? ", ("ml", "l", "g", "kg", "ea"), "unit")
    item_cost = num_check("What is the item cost? ")

    # when called the function works changes g / mL to KG / L
    unit_converter_1 = unit_converter(weight, unit_question)
    # calculate the price per unit
    price_cal = price_calculator(item_cost, unit_converter_1)

    if unit_question == "g":
        unit_final = "kg"
    elif unit_question == "ml":
        unit_final = "l"
    else:
        unit_final = unit_question

    # add item name, weight, cost, unit and $ per kg
    all_item_name.append(item_name)
    all_item_weight.append(unit_converter_1)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_final)
    all_item_per_kg.append(price_cal)
    item_count += 1

if item_count >= 2:
    recommendation_frame = pd.DataFrame(price_comparison_dict)

    recommendation_string = tabulate(recommendation_frame, headers='keys',
                                     tablefmt='psql', showindex=False, numalign="right")
    recommendation_affordability = recommendation(recommendation_frame, budget, "affordability")
    recommendation_lowest_unit = recommendation(recommendation_frame, budget)

    heading = make_statement(f"Price Comparison {day}/{month}/{year}", "-")
    table_heading = "\nHere are the items you are comparing\n"
    table = recommendation_string
    item_heading = f"\nYou are comparing {item_count} items."
    recommendation_heading = "\nHere is my recommendation's for you"
    affordability_heading = "\nHere is the recommendation for items under you budget"
    best_value_heading = "\nHere is the item with the best value for money (items can be over you budget for this)"

    to_write = [heading, table_heading, table, item_heading, recommendation_heading,
                affordability_heading, recommendation_affordability, best_value_heading, recommendation_lowest_unit, ]

    # print area
    print()
    for item in to_write:
        print(item)
    print()
    name = input("What would you like the file name to be? ")
    if name == "":
        name = "Price_comparison"
    print("Good bye")


    # create file to hold data (add .txt extension)
    file_name = f"{name}_{year}_{month}_{day}"
    write_to = "{}.txt".format(file_name)

    text_file = open(write_to, "w+")

    for item in to_write:
        text_file.write(item)
        text_file.write("\n")

elif item_count == 1:
    print("You need at least 2 items to compare.")

else:
    print("No items were entered.")