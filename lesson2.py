def calculate_length(string: str) -> int:
    """Takes a string and returns its length."""
    return len(string)


def join_strings(str1: str, str2: str) -> str:
    """Takes two strings and returns their concatenation."""
    return str1 + str2


def calculate_square(number: int):
    """Takes a number and returns its square."""
    return number ** 2


def calculate_sum(num1: float, num2: float) -> float:
    """Takes two numbers and returns their sum."""
    return num1 + num2


def divide_and_remainder(dividend, divisor) -> tuple:
    """Takes two numbers and performs division. Returns the quotient and remainder."""
    if divisor == 0:
        raise ValueError("Cannot divide by zero.")

    quotient = dividend // divisor
    remainder = dividend % divisor

    return quotient, remainder


def calculate_average(numbers: list) -> float:
    """Takes a list of numbers and calculates their average."""
    if not numbers:
        raise ValueError("The input list is empty.")

    return sum(numbers) / len(numbers)


def find_common_elements(list1: list, list2: list) -> list:
    """Takes two lists and returns a list containing the common elements."""
    return list(set(list1).intersection(set(list2)))


def get_dictionary_keys(input_dict: dict) -> list:
    """Takes a dictionary and prints all its keys."""
    return list(input_dict.keys())


def merge_dictionaries(dict1: dict, dict2: dict) -> dict:
    """Takes two dictionaries and returns a new dictionary that is the union of both dictionaries."""
    dict1.update(dict2)
    return dict1


def merge_sets(set1: set, set2: set) -> set:
    """Takes two sets and returns their union."""
    return set1.union(set2)


def is_subset(set1: set, set2: set) -> bool:
    """Checks if set1 is a subset of set2."""
    return set1.issubset(set2)


def check_parity(number: int) -> str:
    """Checks the parity of the given number."""
    return "Парне" if number % 2 == 0 else "Непарне"


def filter_even_numbers(numbers: list) -> list:
    """Takes a list of numbers and returns a new list containing only even numbers."""
    return list(filter(lambda x: (x % 2 == 0), numbers))


print(
    f"Length: {calculate_length('Some string')}\n"
    f"Concatenation: {join_strings('Orange', 'Juice')}\n"
    f"Square: {calculate_square(12)}\n"
    f"Sum: {calculate_sum(17, 1556)}\n"
    f"Quotient and Remainder: {divide_and_remainder(56, 13)}\n"
    f"Average: {calculate_average([5, 6, 2, 45.3])}\n"
    f"Common Elements: {find_common_elements([5, 6, 2, 45.3], [21, 5, 6])}\n"
    f"Dictionary Keys: {get_dictionary_keys({'key1': 'value1', 'key2': 'value2'})}\n"
    f"Merged Dictionary: {merge_dictionaries({'key1': 'value1', 'key2': 'value2'}, {'key2': 'value2', 'key3': 'value3'})}\n"
    f"Merged Sets: {merge_sets({'apple', 'banana', 'cherry'}, {'apple', 'nuts', 'tomato'})}\n"
    f"Is Subset: {is_subset({'apple', 'banana', 'cherry'}, {'apple', 'nuts', 'tomato'})}\n"
    f"Is Subset: {is_subset({'apple', 'banana'}, {'apple', 'banana', 'cherry'})}\n"
    f"Parity Check: {check_parity(15)}\n"
    f"Parity Check: {check_parity(12)}\n"
    f"Filtered Even Numbers: {filter_even_numbers([4, 5, 78, 23, 21, 17, 15, 46, 12])}"
)
