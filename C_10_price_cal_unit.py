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

def unit(question):
    """checks that the unit is valid and will return """
    while True:
        response = input(question).lower()

        if response == "ml" or response == "l" or response == "g" or response == "kg" or response == "ea":
            return response
        elif response == "":
            return "ea"
        else:
            print("error")

def unit_converter(item_weight, items_unit, unit_price):
    """convert units"""
    if items_unit == "ml" or items_unit == "g":
        print("you are in the ml / g loop")
        item_weight = item_weight / 1000

    per_kg_l = unit_price / weight1
    return per_kg_l

while True:
    weight1 = num_check("what is the weight? ")
    unit_question = unit("What is the unit? ")
    price = num_check("what is the cost? ")
    unit_test = unit_converter(weight1, unit_question)
    # weight1 = num_check("What is the weight? ")
    # unit_question = not_blank("what is the unit? ")
    # unit_cost = num_check("what is the cost? ")
    # unit_test = unit(weight1, unit_question)
    print(unit_test)
    price = price_calculator(unit_test, price)

    print(price, "kg/l/ea")
