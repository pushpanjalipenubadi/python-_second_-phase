choices = ["A", "B", "C"]

def check_valid(choice):
    # Dummy rule: only choices that are not "B" are valid
    return choice != "B"

def choose(choice):
    print(f"Choosing {choice}")

def helpful():
    print("Doing something helpful")

def revert(choice):
    print(f"Reverting {choice}")

def helper():
    for choice in choices:
        if check_valid(choice):
            choose(choice)
            helpful()
            revert(choice)
helper()            
