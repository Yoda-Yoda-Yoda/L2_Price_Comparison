import pandas as pd
from tabulate import tabulate
def num_check(question):
    """checks that the input the user entered is a number more than 0"""
    while True:
        response = input(question).lower()
        try:
            # floats the number
            response = float(response)
            # checks if its over 0
            if response > 0:
                return response
            # throws an error if the input doesn't match any of the above
            else:
                print("Sorry! This needs to be a positive number! Please try again\n")
        except ValueError:
            print("Please enter numbers (Not Letters!)")

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)
        # looks at the user input and checks if it is not blank by using !=
        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def unit(question, valid_ans=("ml", "l", "g", "kg", "ea")):
    """Takes the user answer and checks if it's a valid answer from the list!"""
    while True:
        response = input(question).lower()
        # checks if the user inputted unit is in the list and passes it if it is!
        for item in valid_ans:
            if response == item:
                return item
        # defaults to ea if the user doesn't enter anything
        if response == "":
            return "ea"
        # prints a error
        else:
            print("error")

def unit_price_calculator(item_weight, items_unit, unit_price):
    """convert units and also works out the price per unit"""
    # looks if the item unit is ml or g and then makes it into its l / kg form and if its already in kg / l it'll skip
    if items_unit == "ml" or items_unit == "g":
        print("you are in the ml / g loop")
        item_weight = item_weight / 1000
    # converts it into the price per kg or l or ea
    per_kg_l = unit_price / item_weight
    # rounds the price per kg / l / ea into 2dp
    rounded = round(per_kg_l, 2)
    return rounded

def recommendation(budget, name, weight, cost, unit, unit_cost):
    """Makes a recommendation within budget"""
    if cost <= budget:
        statement = (f"{name} is under the budget you set at ${budget}, this item has a weight {weight} per kg / L / ea\n"
                     f"")



    # if cost <= budget:
    #     statement = f"{name} is under {budget}. At the cost of {cost} for a weight of {weight} a per $ amount of {unit_cost}"
    # else:
    #     statement = (f"There is no items under you budget of {budget}, but the closest item to you budget is\n"
    #                  f"{name} for ${cost} at the weight of {weight} a per $ amount of ${unit_cost}")
    # return statement
# List to hold price details
all_item_name = []
all_item_weight = []
all_item_cost = []
all_item_unit = []
all_item_per_kg = []
# the PANDAS dictionary that will be used in the further down in the program
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
    if unit_question == "g":
        unit_final = "kg"
    elif unit_question == "ml":
        unit_final = "l"
    else:
        unit_final = unit_question
    all_item_weight.append(weight)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_final)
    all_item_per_kg.append(unit_test)

recommendation_frame = pd.DataFrame(price_comparison_dict)
recommendation_string = tabulate(recommendation_frame, headers='keys',
                                 tablefmt='psql', showindex=False)

print(recommendation_string)
recommendation_0 = recommendation_frame.sort_values(by="Unit cost")
print(recommendation_0)
first_row = recommendation_0.iloc[[0]]
print(first_row)
# name = first_row.iloc[0, 0]
# weight = first_row.iloc[0, 1]
# cost = first_row.iloc[0, 2]
# unit = first_row.iloc[0, 3]
# unit_cost = first_row.iloc[0, 4]
# print(name, "\n", weight, "\n", cost, "\n", unit, "\n", unit_cost)
affordability = recommendation_frame[recommendation_frame["Cost"] <= budget]
print(affordability)
if affordability.empty:
    print("list is empty")
lowest_under_budget = affordability.iloc[[0]]
lowest_name = lowest_under_budget.iloc[0, 0]
lowest_weight = lowest_under_budget.iloc[0, 1]
lowest_cost = lowest_under_budget.iloc[0, 2]
lowest_unit = lowest_under_budget.iloc[0, 3]
lowest_unit_cost = lowest_under_budget.iloc[0, 4]
recommendation_result = recommendation(budget, lowest_name, lowest_weight, lowest_cost, lowest_unit, lowest_unit_cost)
print(recommendation_result)
