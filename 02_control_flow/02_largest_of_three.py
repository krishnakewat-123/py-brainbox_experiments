'''####### output #############
Enter first number: 2
Enter second number: 5
Enter third number: 6
Largest: 6
##############################
'''
a = int(input("Enter first number: ")) # taking user input
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:# logic implementation
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)
