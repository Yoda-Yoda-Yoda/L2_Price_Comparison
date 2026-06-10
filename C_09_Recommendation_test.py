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

def unit_price_calculator(item_weight, items_unit, unit_price):
    """convert units and also works out the price per unit"""
    if items_unit == "ml" or items_unit == "g":
        print("you are in the ml / g loop")
        item_weight = item_weight / 1000

    per_kg_l = unit_price / item_weight
    rounded = round(per_kg_l, 2)
    return rounded

def recommendation(budget, name, weight, cost, unit, unit_cost):
    """Makes a recommendation within budget"""
    if cost <= budget:
        statement = f"{name} is under {budget}. At the cost of {cost} for a weight of {weight} a per $ amount of {unit_cost}"
    else:
        statement = (f"There is no items under you budget of {budget}, but the closest item to you budget is\n"
                     f"{name} for ${cost} at the weight of {weight} a per $ amount of ${unit_cost}")
    return statement
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
    unit_test = unit_price_calculator(weight, unit_question, item_cost)
    all_item_name.append(item_name)


    all_item_weight.append(weight)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_question)
    all_item_per_kg.append(unit_test)

recommendation_frame = pd.DataFrame(price_comparison_dict)
recommendation_string = tabulate(recommendation_frame, headers='keys',
                                 tablefmt='psql', showindex=False)

print(recommendation_string)
recommendation_0 = recommendation_frame.sort_values(by="Unit cost")
print(recommendation_0)
first_row = recommendation_0.iloc[[0]]
print(first_row)
name = first_row.iloc[0, 0]
weight = first_row.iloc[0, 1]
cost = first_row.iloc[0, 2]
unit = first_row.iloc[0, 3]
unit_cost = first_row.iloc[0, 4]
print(name, "\n", weight, "\n", cost, "\n", unit, "\n", unit_cost)
affordability = recommendation_frame[recommendation_frame["Cost"] <= budget]
print(affordability)
if affordability.empty:
    print("list is empty")
recommendation_result = recommendation(budget, name, weight, cost, unit, unit_cost)
print(recommendation_result)
