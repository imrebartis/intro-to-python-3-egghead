import sys

# print(int(sys.argv[1]) / int(sys.argv[2]))

# terminal: python3 errors.py 4 2
# => 2.0

try:
    print(int(sys.argv[1]) / int(sys.argv[2]))
except ValueError as e:
    print('You must enter a valid number')
except ZeroDivisionError as e:
    print("You can't divide by zero")