#Drake Pierce-Demski
#

# FizzBuzz Program
def fizzbuzz():
    for num in range(1, 16):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizzbuzz()

# Scholarship Eligibility Checker
def scholarship_eligibility():
    gpa = float(input("Enter your GPA: "))
    credits = int(input("Enter your total credits: "))

    is_eligible = (gpa > 3.5) and (credits > 60)
    print(is_eligible)

scholarship_eligibility()

# Find the Maximum of Three Numbers
def find_maximum():
    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    num3 = float(input("Third number: "))

    maximum = num1  # Assume num1 is the largest initially

    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3

    print(maximum)

find_maximum()