def safe_divide(numerator, denominator):
    try:
        
        numerator = float(numerator)
        denominator = float(denominator)
        
        
        result = numerator / denominator
        
        
        return result
        
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    except ValueError:
        return "Error: Both numerator and denominator must be numeric."