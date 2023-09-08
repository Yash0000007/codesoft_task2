while True:
    a = int(input("Enter a number : "))
    b = int(input("Enter a number : "))
    print("Enter 1 for Addition    2 for Subtraction    3 for Multiply    4 for Division    5 to Exit")
    ch = int(input("Enter choice : "))
    
    if ch == 1:
        print("Sum of", a, "+", b, "=", a + b)
    elif ch == 2:
        print("Difference of", a, "-", b, "=", a - b)
    elif ch == 3:
        print("Product of", a, "*", b, "=", a * b)
    elif ch == 4:
        if b != 0:
            print("Division of", a, "/", b, "=", a / b)
        else:
            print("Division by zero is not allowed.")
    elif ch == 5:
        print("Exiting the program.")
        break
    else:
        print("Wrong choice")
