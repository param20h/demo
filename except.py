try:
    x = int(input("Enter number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid number!")
else:
    print("No errors occurred.")
finally:
    print("This always runs.")
