'''####### output ##########
Enter total number of element:4
Enter a number: 1
Enter a number: 2
Enter a number: 3
Enter a number: 5
Largest number: 5
########## end ##########'''

def find_largest(lst):
    largest = lst[0]
    i = 1

    while i < len(lst):
        if lst[i] > largest:
            largest = lst[i]
        i += 1

    return largest

num=[]
n=int(input("Enter total number of element:"))
for i in range(n):
    num.append(int(input("Enter a number: ")))
print("Largest number:", find_largest(num))
