def string_checker(question, valid_ans=('yes', 'no')):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        user_response = input(question).lower()

        for item1 in valid_ans:
            # check if the user response is a word in the list
            if item1 == user_response:
                return item1

            # check if the user response it the same as
            # the first letter of an item in the list
            elif user_response == item1[0]:
                return item1

        if user_response == "":
            return "ea"

        # print error if user doesn't enter something that's valid
        print(error)
        print()