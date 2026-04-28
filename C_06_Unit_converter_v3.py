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

weight1 = num_check("What is the weight? ")
unit_question = not_blank("what is the unit? ")

unit_test = unit(weight1, unit_question)
print(unit_test, "kg/L")