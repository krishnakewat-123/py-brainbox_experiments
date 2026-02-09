'''######### output ###########
Even numbers: [2, 4, 6]
Squares: [1, 4, 9, 16, 25, 36]
'''########## end #############
def main():
    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = [num for num in numbers if num % 2 == 0]
    squares = [num ** 2 for num in numbers]

    print("Even numbers:", even_numbers)
    print("Squares:", squares)


if __name__ == "__main__":
    main()
