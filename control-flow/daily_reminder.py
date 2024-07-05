task = input("Enter the task describtioin: ")
priority = input("Enter the task priority (high, medium, low): ")
time_bound = input("Is the task time-bond? (yes or no): ")

print("\nReminder:")
match priority.lower():
    case 'high':
        print(f"Task: '{task}' is a high priority.")
    case 'medium':
        print(f"Task: '{task}' is a medium priority.")
    case 'low':
        print(f"Task: '{task}' is a low priority.")
        
if time_bound.lower() ==  'yes':
    print(f"This task requires immediate attention today!")
else:
    print(f"this task does not have an immediate time constraint.")    