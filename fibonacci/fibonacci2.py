# n = input("Please insert number here: ")

# dictionary

fibonacci_dict = {0: 0, 1: 1}

def fibonacci_improved(n):
    if fibonacci_dict.get(n) is not None:
        return fibonacci_dict.get(n)
    else:
        result = fibonacci_improved(n-1) + fibonacci_improved(n-2)
        fibonacci_dict[n] = result
        return result
print (fibonacci_improved(999))
