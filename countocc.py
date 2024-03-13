def count_occurrences(string):
    """
    Counts the occurrences of each alphabetic character in a given string.

    Args:
        string (str): The input string to count occurrences from.

    Returns:
        dict: A dictionary containing the count of each alphabetic character in the string.
    """
    occurrences = {}  # Create an empty dictionary to store the occurrences of each character
    for letter in string:  # Iterate through each character in the string
        if letter.isalpha():  # Check if the character is alphabetic
            occurrences[letter] = occurrences.get(letter, 0) + 1  # Increment the count of the character in the dictionary
    return occurrences  # Return the dictionary containing the occurrences



print(count_occurrences("testthisstring"))
print(count_occurrences("what about this one?"))