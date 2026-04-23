from datetime import date
# functions goes here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
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

def unit(weight, unit_1):
    """convert units"""
    number = weight
    unit_name = unit_1
    while True:
        if unit_name == "ml" or unit_name == "g":
            print("you are in the ml / g loop")
            number = number / 1000
            return number
        elif unit_name == "l" or unit_name == "kg":
            print("you are in the l / kg loop")
            return number
        else:
            print("Please enter a number / unit")

def price_calculator(weight, unit_price):
    """Calculates the cost per kg/L from the unit cost"""
    per_kg_l = unit_price / weight
    return per_kg_l
# main routine starts here

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
while True:
    # gets the response from the user for the calculator
    weight_1 = num_check("what is the weight? ")
    unit_cost = num_check("what is the cost")
    unit_question = not_blank("What is the unit? ")
    if weight_1 == "xxx" or unit_cost == "xxx" or budget == "xxx":
        break
    unit = unit(weight_1, unit_question)
    print(unit, "kg")
    price_per_weight = price_calculator(weight_1, unit_cost)
    # testing
    print(f"${price_per_weight} / {unit_question}")

print("you have broken the loop😭😭😭")