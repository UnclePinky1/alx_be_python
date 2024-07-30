class Calculator:
    calculation_type = "Arithmetic Operations"
    
    def add(a, b):
        """Static method to return the sum of two numbers."""
        return a + b
    
    def multiply(cls, a, b):
        """Class method to return the product of two numbers and print the class attribute."""
        print(f"Calculation Type: {cls.calculation_type}")
        return a * b
    