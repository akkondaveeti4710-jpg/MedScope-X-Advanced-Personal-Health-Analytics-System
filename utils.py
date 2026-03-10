def ask_float(question):

    while True:
        try:
            return float(input(question))
        except:
            print("Invalid number")


def ask_int(question):

    while True:
        try:
            return int(input(question))
        except:
            print("Invalid number")


def ask_yes_no(question):

    while True:

        ans = input(question + " (yes/no): ").lower()

        if ans in ["yes","y"]:
            return True

        if ans in ["no","n"]:
            return False

        print("Please answer yes or no")
