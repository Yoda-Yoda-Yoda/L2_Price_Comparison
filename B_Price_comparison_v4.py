from datetime import date
# functions goes here
def make_statement(statement, decoration):
    """Emphasizes headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def yes_no(question):
    """Checks that users entered yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
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

        if response == "xxx":
            return response

        try:
            response = float(response)

            if response > 0:
                return response
            elif response < 0:
                error = "Please enter a positive number"
                print(error)
        except ValueError:
            print("Please enter numbers (Not Letters!)")

def unit(question, valid_ans=("ml", "l", "g", "kg", "ea")):
    """Takes the user answer and checks if it's a valid answer from the list!"""
    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item:
                return item

        if response == "":
            return "ea"
        else:
            print("error")

def unit_converter(item_weight, items_unit):
    """convert units"""
    while True:
        if items_unit == "ml" or items_unit == "g":
            print("you are in the ml / g loop")
            item_weight = item_weight / 1000
        elif items_unit == "l" or items_unit == "kg":
            print("you are in the l / kg loop")
        elif items_unit == "ea":
            print("you are in the each world")
        else:
            print("Please enter a number / unit")

        return item_weight

def price_calculator(weight1, unit_price):
    """Calculates the cost per kg/L from the unit cost"""
    per_kg_l = unit_price / weight1
    return per_kg_l
# main routine starts here

# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []

price_comparison_dict = {
    'Name': all_item_name,
    'Weight': all_item_weight,
    'Cost': all_item_cost,
    'Unit': all_item_unit
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

budget = num_check("What is your budget? ")
# while True:
#     item_name = not_blank("What is the item name? ")
#     weight_1 = num_check("what is the weight? ")
#     unit_cost = num_check("what is the cost? ")
#     unit_question = not_blank("What is the unit? ")
#     if item_name == "xxx" or weight_1 == "xxx" or unit_cost == "xxx" or budget == "xxx":
#         break
#     unit = unit(weight_1, unit_question)
#     print(unit, "kg")
#     price_per_weight = price_calculator(weight_1, unit_cost)
#     # testing
#     print(f"${price_per_weight} / {unit_question}")
#     # add item name, item weight, item cost and unit
#     all_item_name.append(item_name)
#     all_item_weight.append(weight_1)
#     all_item_cost.append(unit_cost)
#     all_item_unit.append(unit_question)
# print("you have broken the loop😭😭😭")

while True:
    item_name = not_blank("What is the item name? ")
    weight = num_check("What is the weight? ")
    unit_question = unit("what is the unit? ")
    item_cost = num_check("What is the item cost? ")
    unit_test = unit_converter(weight, unit_question)
    # changes mL / g to L / KG
    price_per_weight = price_calculator(unit_test, item_cost)

    # add item name, item weight, item cost and unit
    all_item_name.append(item_name)
    all_item_weight.append(weight)
    all_item_cost.append(item_name)
    all_item_unit.append(unit_question)