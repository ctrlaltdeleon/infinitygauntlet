def test_function() -> None:
    print("Testing the module if it works.")


def find_maximum_number(numbers: list) -> int:
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
