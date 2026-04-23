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

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def price_calculator(weight, unit_price):
    """Calculates the cost per kg/L from the unit cost"""
    per_kg_l = unit_price / weight
    return per_kg_l

while True:
    weight_1 = num_check("what is the weight? ")
    unit_cost = num_check("what is the cost")
    unit = not_blank("What is the unit? ")
    price_per_weight = price_calculator(weight_1, unit_cost)
    # testing
    print(price_per_weight)
