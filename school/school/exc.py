try:
    num = int(input("Enter a number: "))
    
    if num == 0:
        raise ValueError("Number should not be zero")

    assert num % 2 == 0, "Number is not even"

except ZeroDivisionError:
    print("Division by zero")

except ValueError as ve:
    print(f"ValueError: {ve}")

except AssertionError as ae:
    print(f"AssertionError: {ae}")

else:
    reciprocal = 1 / num
    print(f"The reciprocal of {num} is: {reciprocal}")
