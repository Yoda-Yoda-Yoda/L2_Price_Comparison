def int_check(question):
    """Checks that users enter an integer between two values"""


    error = "Oops - please enter an integer"

    while True:
        response = input(question).lower()

        # checks for the exit code
        if response == "xxx":
            return response

        try:
            # Change the response to an integer and check that it's more than zero
            response = int(response)
            if response < 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

test = int_check("how many? ")
print(test)