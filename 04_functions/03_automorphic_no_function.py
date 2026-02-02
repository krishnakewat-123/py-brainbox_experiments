'''##### output##########
Enter a number: 25
Automorphic Number
###### end #############'''
def is_automorphic(num):
    square = num * num

    while num > 0:
        if num % 10 != square % 10:
            return False
        num //= 10
        square //= 10

    return True


number = int(input("Enter a number: "))
print("Automorphic Number" if is_automorphic(number) else "Not an Automorphic Number")
