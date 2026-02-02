'''###### output ############
Enter a number: 1124
Spy Number
########## end ############'''
def is_spy(num):
    total = 0
    product = 1

    while num != 0:
        digit = num % 10
        total += digit
        product *= digit
        num //= 10

    return total == product


number = int(input("Enter a number: "))
print("Spy Number" if is_spy(number) else "Not a Spy Number")
