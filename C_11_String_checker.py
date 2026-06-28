def string_check(question, valid_ans=None, item_type=None):
    """Takes the user answer and checks if it's a valid answer from the list!"""
    while True:
        response = input(question).lower()
        # checks if the item is in the list
        for item_unit in valid_ans:
            if response == item_unit:
                return item_unit
        # if the user inputs <blank> then the program will
        # presume the user wants each
        if item_type == "unit":
            if response == "":
                return "ea"
            else:
                print("error")

