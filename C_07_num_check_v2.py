def num_check(question, min_number=0):
    """checks that the input the user entered is a number more than 0"""
    while True:
        response = input(question).lower()
        try:
            response = float(response)
            # checks if the user response is greater then 0
            if response > min_number:
                return response
            # if the response is under 0 the program will return an error
            else:
                error = f"Please enter a number that is above {min_number}"
                print(error)
        except ValueError:
            print("Please enter numbers (Not Letters!)")

while True:
    # question = num_check("Please enter a number! ")
    question = num_check("Budget? ", 20)
    print(question)
