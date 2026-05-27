import pandas as pd
from tabulate import tabulate
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
            else:
                print("Sorry! This needs to be a positive number! Please try again\n")
        except ValueError:
            print("Please enter numbers (Not Letters!)")

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

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
    if items_unit == "ml" or items_unit == "g":
        print("you are in the ml / g loop")
        item_weight = item_weight / 1000

    return item_weight

def price_calculator(weight1, unit_price):
    """Calculates the cost per kg/L from the unit cost"""
    per_kg_l = unit_price / weight1
    return f"{per_kg_l}:.2f"

def recommend(item_name_1, item_price_unit, budget_1):
    """Recommend the best value for money"""
    print(item_price_unit)
    lowest_price = min(item_price_unit)

    return lowest_price


# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []
all_item_per_kg = []

price_comparison_dict = {
    'Name': all_item_name,
    'Weight': all_item_weight,
    'Cost': all_item_cost,
    'Unit': all_item_unit,
    'Unit cost': all_item_per_kg
}
budget = num_check("What is your budget? ")
while True:
    item_name = not_blank("What is the item name? ")
    if item_name == "xxx":
        break
    weight = num_check("What is the weight? ")
    unit_question = unit("what is the unit? ")
    item_cost = num_check("What is the item cost? ")
    unit_test = unit_converter(weight, unit_question)
    # changes mL / g to L / KG
    price_per_weight = price_calculator(unit_test, item_cost)

    all_item_name.append(item_name)
    all_item_weight.append(weight)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_question)
    all_item_per_kg.append(price_per_weight)

recommendation_frame = pd.DataFrame(price_comparison_dict)
recommendation_string = tabulate(recommendation_frame, headers='keys',
                                 tablefmt='psql', showindex=False)
print(recommendation_string)
# recommendation = recommend(all_item_name, all_item_per_kg, budget)
# print(recommendation)