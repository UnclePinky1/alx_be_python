size = int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Size should be a positive integer.")
else:
    row = 1
    while row <= size:
        for column in range(size):
            print("*", end="")
            
            print()
            row += 1