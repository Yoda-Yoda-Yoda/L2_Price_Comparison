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

def unit_converter(item_weight, item_unit):
    """convert grams or ml to kg and l"""
    if item_unit == "ml" or item_unit == "g":
        item_weight = item_weight / 1000
    else:
        item_weight = item_weight
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
    affordability_1 = affordability.sort_values(by="Cost")
    lowest_under_budget = affordability_1.iloc[[0]]
    # cheapest unit area
    recommendation_0 = (df.sort_values(by="Unit cost"))
    cheapest_unit = recommendation_0.iloc[[0]]
    if type_1 == "affordability":
        list_1 = lowest_under_budget
    else:
        list_1 = cheapest_unit

    name = list_1.iloc[0, 0]
    weight_1 = list_1.iloc[0, 0]
    cost = list_1.iloc[0, 0]
    unit_1 = list_1.iloc[0, 0]
    unit_cost = list_1.iloc[0, 0]

    # return area
    if type_1 == "affordability":
        output = (f"{name} is the cheapest item in your comparison at ${cost} for for {weight_1} / {unit_1} with a price"
                  f"per {unit_1} at {unit_cost}")
    elif type_1 == "cheapest":
        output =

    else:
        output = "List is empty "

    return output
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
    unit_converter_1 = unit_converter(weight, unit_question)
    price_cal = price_calculator(item_cost, unit_converter_1)

    all_item_name.append(item_name)
    if unit_question == "g":
        unit_final = "kg"
    elif unit_question == "ml":
        unit_final = "l"
    else:
        unit_final = unit_question

    all_item_weight.append(unit_converter_1)
    all_item_cost.append(item_cost)
    all_item_unit.append(unit_final)
    all_item_per_kg.append(price_cal)

recommendation_frame = pd.DataFrame(price_comparison_dict)
recommendation_string = tabulate(recommendation_frame, headers='keys',
                                 tablefmt='psql', showindex=False, numalign="right")
recommendation_affordability = recommendation(recommendation_frame, budget, "affordability")
print(recommendation_affordability)
recommendation_lowest_unit = recommendation(recommendation_frame, budget)
print(recommendation_lowest_unit)
