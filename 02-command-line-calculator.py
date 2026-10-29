import sys 
if len(sys.argv) !=4:
    print("Usage: python3 02-command-line-calculator.py <number1> <operator> <number2>")

print(sys.argv)

try:
    first_number = int(sys.argv[1])
    second_number = int(sys.argv[3])
except ValueError:
    print("Error: Please enter Valid integers.")
    sys.exit(1)


operator = sys.argv[2]


print(f"First Number : {first_number}")
print(f"Operator: {operator}")
print(f"Second Number: {second_number}")
if operator == "+":
    print(f"Result: {first_number + second_number}")
elif operator == "-":
    print(f"Result : {first_number - second_number}")
elif operator == "*":
    print(f"Result: {first_number*second_number}")
elif operator == "/":
    if second_number == 0:
        print("error: cannot divide by zero")
    else:
        print(f"Result: {first_number / second_number}")
else:
    print("Invalid Operator")
    sys.exit(1)



# When testing multiplication in your Mac terminal, use quotes:
# python3 02-command-line-calculator.py 10 "*" 5
