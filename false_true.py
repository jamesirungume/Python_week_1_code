def false_true(a, b, c):
    result = 0
    
    if a > 0:
        result += 1
    if b > 0:
        result += 1
    if c > 0:
        result += 1
        
    print(f"Positive numbers count: {result == 2}")
    return result == 2

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))

false_true(a, b, c)
