def string_checker(question, valid_ans=None, string_type=None):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # Get user response and make sure it's lowercase
        response = input(question).lower()

        for item1 in valid_ans:
            # check if the user response is a word in the list
            if item1 == response:
                return item1

            # check if the user response it the same as
            # the first letter of an item in the list
            elif response == item1[0]:
                return item1

        if string_type == "unit":
            if response == "":
                return "ea"
        # print error if user doesn't enter something that's valid
        print(error)
        print()

while True:
    # yes_no = string_checker("do you want instructions?", ("yes", "no"))
    # print(yes_no)

    unit = string_checker("what unit? ", ("ml", "l", "g", "kg", "ea"), "unit")
    print(unit)