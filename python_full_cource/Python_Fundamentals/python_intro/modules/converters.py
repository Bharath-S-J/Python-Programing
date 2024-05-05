def lbs_to_kg(weight):
    """
    Convert weight from pounds to kilograms.

    Parameters:
    weight (float or int): Weight in pounds to be converted.

    Returns:
    float: Weight in kilograms.
    """
    return weight * 0.45


def kg_to_lbs(weight):
    """
    Convert weight from kilograms to pounds.

    Parameters:
    weight (float or int): Weight in kilograms to be converted.

    Returns:
    float: Weight in pounds.
    """
    return weight / 0.45


def find_max(numbers):
    """
    Find the maximum value in a list of numbers.

    Parameters:
    numbers (list): List of numbers.

    Returns:
    float or int: Maximum value in the list.
    """
    # Initialize 'max' with the first element of 'numbers'
    max_value = numbers[0]

    # Iterate through each number in the list
    for number in numbers:
        # Update 'max_value' if the current number is greater
        if number > max_value:
            max_value = number

    return max_value
