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

def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def unit(question):
    while True:
        response = input(question)

        if response == "ml" or response == "l" or response == "g" or response == "kg":
            return response
        else:
            print("entering the each world")
            if response != "each" or response != "ea":
                question1 = yes_no("are you wanting $/each? ")
                if question1 == "yes":
                    return "each"

def unit_converter(item_weight, items_unit):
    """convert units"""
    while True:
        if items_unit == "ml" or items_unit == "g":
            print("you are in the ml / g loop")
            item_weight = item_weight / 1000
        elif items_unit == "l" or items_unit == "kg":
            print("you are in the l / kg loop")
        else:
            print("Please enter a number / unit")

        return item_weight

weight = num_check("What is the weight? ")
unit_question = unit("what is the unit? ")

unit_test = unit_converter(weight, unit_question)
print(unit_test)