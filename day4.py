
colors = ["red","blue","yellow","green","violet","orange", "black", "white","pink", "purple","grey","brown","silver","gold","bronze","light","dark","cream","peach","mustard","magenta","cyan","orange","indigo","pink","teal","lime","maroon","navy","olive","teal","violet","white","yellow"]
print(colors[:])
# 0 and infinity
animals =['dog', 'cat', 'bird', 'cow']
print(animals[0:3])

vehicles = 'airplane'
new_vehicles = vehicles[2:4]
print(new_vehicles)
if new_vehicles == 'air':
    print(True)
else:
    print(False) 



print("Simple Calculator")
num1 = int(input())
num2 = int(input())
arr = ['add', 'subtract', 'multiply', 'divide']
for i in range(4):
    print(i + 1, arr[i])
print("Input operation:")
op = int(input())
print("Result:")
if op == 1:
    print(num1 + num2)
elif op == 2:
    print(num1 - num2)
elif op == 3:
    print(num1 * num2)
elif op == 4:
    print(num1 / num2)
else:
    print("Invalid number, please try again!")