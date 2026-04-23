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
def unit(question):
    """convert units"""
    number = num_check(question)
    unit_name = input("What unit? ").lower()
    if unit_name == "ml" or unit_name == "g":
        print("you are in the ml / g if")
        number = number / 1000
        return number
    elif unit_name == "l" or unit_name == "kg":
        print("you are in the l / kg loop")
        return number
    else:
        print("Please enter a number / unit")

unit_test = unit("Number? ")
print(unit_test)