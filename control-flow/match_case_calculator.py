num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

results = 0 
if operator == "+":
    results = num1 + num2 
elif operator == "-":
    results =  num1 - num2 
elif operator == "*":
    results = num1 * num2 
elif operator == "/":
    if num2 == 0:
     print("Division by zero error")
     exit() 
    result = num1 / num2
else:
    print("Invalid operator")
    exit()       
    
print("The result is", results)    

                        