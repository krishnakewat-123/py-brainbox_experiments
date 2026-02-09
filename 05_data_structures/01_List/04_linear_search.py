'''######## output ##########
Sorted list: [1, 2, 5, 8, 9]
8 found at index 3
'''######## end ############
def linear_search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i
    return -1


def main():
    numbers = [5, 2, 8, 1, 9]

    numbers.sort()
    print("Sorted list:", numbers)

    target = 8
    index = linear_search(numbers, target)

    if index != -1:
        print(f"{target} found at index {index}")
    else:
        print(f"{target} not found")


if __name__ == "__main__":
    main()
