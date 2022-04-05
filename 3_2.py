

# grade = 90


# if grade >= 90:
#     #execute this
#     print("Your grade is A")
# else:
#     print("Your grade is not A")

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

if isinstance(num1, str) or isinstance(num2, str):
    print("Input not allowed input a numeric number")
else:
    num1 = eval(num1)
    num2 = eval(num2)
    
# if isinstance(num1, str)
# if isinstance
# if num1 > num2:
#     largerValue = num1
# else: 
#     largerValue = num2
# print("The larger value is", str(largerValue) + ".")