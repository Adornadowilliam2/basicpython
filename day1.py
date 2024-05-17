#how to print hello world in python
print("Hello World")
#for create a break line
print("\n========")


#how to initialize something
myage = 19
myname = "William"


#how to create a condition statement
if myage == 18:
    print("You're lying!")
elif myage < 18:
    print("You're good!")
elif myage > 18 and myname == "William":
    print("That's the right one!")
else:
    print("Oh hell nah!")


gojo = True
authorname = "Gege"


if gojo == True and authorname == "Gege":
    msg = "He is alive"
elif gojo == False:
    msg = "You're hallucinated"
else:
    msg = "Just a fandom addiction"
print("What do you think chapter 236? " + msg)


#then how can i able to print this variable
# simple just use print()
print(authorname)


#form activity
name = "John Cena"
age = 18
address = "Rosario Pasig City"
grade = "College"
birthdate = "May 6, 2005"

name = "John Cena"
age = 18
address = "Rosario Pasig City"

# Concatenate strings using the + operator
print("Hello my name is " + name + "\nI am " + str(age) + "\nI live in " + address)
