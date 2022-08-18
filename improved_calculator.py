def calculator():
    operators = ["+", "-", "*", "/"]
    while True:
        try: 
             num_1 = float(input("First Nummber: "))
             print(operators)
             operation = input("Choose an operator from above: ")
             num_2 = float(input("Second Number: "))

        except:
            print("Not a Number. Try again")

        if operation == operators[0]:
            print(num_1 + num_2)
        elif operation == operators[1]:
             print(num_1 - num_2)
        elif operation == operators[2]:
             print(num_1 * num_2)
        elif operation == operators[3]:
             print(num_1 / num_2)
    return
calculator()
