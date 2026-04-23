def num_check(question):
    """checks that the input the user entered is a number more than 0"""
    error = "Please enter numbers (Not Letters!)"
    while True:
        response = input(question).lower()

        if response == "xxx":
            return response

        try:
            response = float(question)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


question = num_check("Please enter a number! ")
print(question)
