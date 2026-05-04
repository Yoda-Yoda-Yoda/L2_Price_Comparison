def not_blank(question):
    """Checks that a user input isn't blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry! this can't be blank. Please try again\n")

def unit(question):
    while True:
        response = input(question).lower()

        if response == "ml" or response == "l" or response == "g" or response == "kg" or response == "ea":
            return response
        elif response == "":
            return "ea"
        else:
            print("error")

while True:
    question1 = unit("what unit? ")
    print(question1)