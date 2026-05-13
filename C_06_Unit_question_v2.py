def unit(question, valid_ans=("ml", "l", "g", "kg", "ea")):
    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item:
                return item

        if response == "":
            return "ea"
        else:
            print("error")

while True:
    question1 = unit("what unit? ")
    print(question1)