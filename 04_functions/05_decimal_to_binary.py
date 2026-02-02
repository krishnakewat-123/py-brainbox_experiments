'''###### outtput ##########
Enter a decimal number: 4
Binary: 100
######## end ########## '''
def decimal_to_binary(num):
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary


number = int(input("Enter a decimal number: "))
print("Binary:", decimal_to_binary(number))
