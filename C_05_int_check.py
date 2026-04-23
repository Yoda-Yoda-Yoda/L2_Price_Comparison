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

            return response

        except ValueError:
            print(error)

int_check("how many? ")