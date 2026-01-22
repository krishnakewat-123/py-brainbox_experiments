'''####### output ###########
Enter a number: 4
Factorial: 24
'''######### end ############
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):# for loop will run till (n+1)-1
    fact *= i

print("Factorial:", fact)
