'''##### output #######
Enter a number: 153
Armstrong Number
######### end #########'''
num = int(input("Enter a number: "))
temp = num
sum_of_powers = 0

# logic to count number of digits
digits = 0
n = num
while n != 0:
    digits += 1
    n //= 10

#logic to calculate sum of powers of digits
while num != 0:
    digit = num % 10
    sum_of_powers += digit ** digits
    num //= 10

if sum_of_powers == temp:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
