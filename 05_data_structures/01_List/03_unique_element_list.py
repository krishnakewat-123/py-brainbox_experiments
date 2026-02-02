'''###### output ######
Enter total number of elements: 3
Enter number: 4
Enter number: 2
Enter number: 4
Unique list: [4, 2]
######### end ########'''
def remove_duplicates(lst):
    unique = []

    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique
numbers = []
num = int(input("Enter total number of elements: "))

for i in range(num):
    j = int(input("Enter number: "))
    numbers.append(j)
print("Unique list:", remove_duplicates(numbers))
