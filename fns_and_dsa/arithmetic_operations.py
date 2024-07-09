def perform_operations(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'devide':
        if num2 == 0:
            return "Division by zero is not allowed."
        else:
            return num1 /  num2
        
    else:
        return "Invalid operation. please choose from 'add', 'subtarct', 'muultiply', or 'dvide'."
    