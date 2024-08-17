variable = 5/2
print(variable)

num = 360
print(type(num))


print("")
print("Welcome to Python calulator")
print("Input num1:")
num1 = int(input())
print("Input num2:")
num2 = int(input())
print("1.) plus \n2.) minus \n3.) times \n4.) divide")
print("Input operation:")

op = int(input())
if op == 1:
    print("Total", num1 + num2)
elif op == 2:
    print("Total", num1 - num2)
elif op == 3:
    print("Total", num1 * num2)
elif op == 4: 
    print("Total", num1 / num2)
else:
    print("Invalid number, please try again!")
    

animal = "DOG"
print(animal[0])

x = "arctic"


# now i know that is possible to print only a part of a string
print(x[2] + x[0] + x[3])