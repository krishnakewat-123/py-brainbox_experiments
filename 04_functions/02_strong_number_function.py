'''######## output ########
Enter a number: 145
Strong Number
######## end ########'''
def is_strong(num): # this is function
    temp = num
    total = 0

    while num != 0: 
        digit = num % 10  # geting last digit

        fact = 1
        i = 1
        while i <= digit: # factorial calculation of digits
            fact *= i
            i += 1

        total += fact
        num //= 10

    return total == temp


number = int(input("Enter a number: "))
print("Strong Number" if is_strong(number) else "Not a Strong Number")
