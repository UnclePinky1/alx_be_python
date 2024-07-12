def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
                
        choice = input("Please choose an option (1-4): ")
        
        
        if choice == '1':
            item = input("Enter the name of the item to add: ")
            shopping_list.append(item)
            print("f{item} has been added to the shopping list.")
            
        elif choice == '2':
            item = input("Enter the name of the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print("f{item} has been removed from the shopping list.")
            else:
                print(f"{item} is not in the shopping list.")
                
        elif choice == '3':
            print("\nCurrent shopping list: ")
            if shopping_list:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                else:
                    print("The shopping list is currently empty.")
                    
                    
        elif choice == '4':
            print("Exiting the shopping list program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please select a valid option (1-4).")
            
if __name__ == "_main_":
    main()     