'''######### output ###########
Enter first number: 1
Enter second number: 2
1.Add  2.Subtract  3.Multiply
Choose option: 1
Ans.=3
############## end ##############
'''
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("1.Add  2.Subtract  3.Multiply")
choice = int(input("Choose option: "))
if choice == 1:
    print("Ans.=",a + b)
elif choice == 2:
    print("Ans.=",a - b)
elif choice == 3:
    print("Ans.=",a * b)
else:
    print("Invalid choice")
