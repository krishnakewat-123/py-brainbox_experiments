'''######## output #######
Enter a number: 4
Sum: 10
##########################
'''
n = int(input("Enter a number: "))
total= 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)
