'''######### output #########
  Largest number: 89
########### end #############
'''
numbers = [10, 45, 23, 89, 12]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number:", largest)
