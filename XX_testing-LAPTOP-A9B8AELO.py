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

def recommendation(df, budget_0):
    """Makes a recommendation within budget"""
    recommendation_0 = (df.sort_values(by="Unit cost"))
    print(recommendation_0)
    affordability = df[df["Cost"] <= budget_0]
    if not affordability.empty:
        affordability_1 = affordability.sort_values(by="Cost")
        lowest_under_budget = affordability_1.iloc[[0]]
        lowest_name = lowest_under_budget.iloc[0, 0]
        lowest_weight = lowest_under_budget.iloc[0, 1]
        lowest_cost = lowest_under_budget.iloc[0, 2]
        lowest_unit = lowest_under_budget.iloc[0, 3]
        lowest_unit_cost = lowest_under_budget.iloc[0, 4]
        print("testing", lowest_under_budget, "\n", lowest_name, lowest_weight, lowest_cost, lowest_unit, lowest_unit_cost)
    else:
        print("List is empty")

    cheapest_unit = recommendation_0.iloc[[0]]
    print(cheapest_unit)
    cheapest_name_unit = cheapest_unit.iloc[0, 0]
    cheapest_weight_unit = cheapest_unit.iloc[0, 1]
    cheapest_cost_unit = cheapest_unit.iloc[0, 2]
    cheapest_unit_unit = cheapest_unit.iloc[0, 3]
    cheapest_cost_cost_unit = cheapest_unit.iloc[0, 4]
    print("hello", cheapest_name_unit, cheapest_weight_unit, cheapest_cost_unit, cheapest_unit_unit,
          cheapest_cost_cost_unit)


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
recommendation_result = recommendation(recommendation_frame, budget)
print(recommendation_result)
