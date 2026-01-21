'''######## output ##############
Enter principal amount: 100
Enter rate of interest (in %): 4
Enter time period (in years): 2
Simple Interest is: 8.0
########### end ################
'''
# This program calculates simple interest

# Taking input
principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest (in %): "))
time = float(input("Enter time period (in years): "))

# Calculating simple interest
simple_interest = (principal * rate * time) / 100

#simple interest
print("Simple Interest is:", simple_interest)
