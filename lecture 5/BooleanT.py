# a = True 
# b = False 

# print(a)
# print(b)

# result = 10 > 5
# print(result)

try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
except ValueError:
    print("That's not a valid number!")