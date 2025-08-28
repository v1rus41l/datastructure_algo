def search(list, target):
    """
    Return the index position of the target of found,
    else returns None
    """
    start = 0
    end = len(list) - 1

    while start <= end:
        midpoint = (start + end) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            end = midpoint - 1
        else:
            start = midpoint + 1
    return None


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(search(numbers, 4))  ## returns 3
    print(search(numbers, 9))  ## returns 8
    print(search(numbers, 11))  ## return None
