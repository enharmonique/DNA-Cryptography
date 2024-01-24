import random


def generate_random_dna_sequence(length):
    """
    Generates a random DNA sequence of the specified length.

    Parameters:
    - length (int): The length of the DNA sequence.

    Returns:
    - str: Random DNA sequence.
    """
    return ''.join(random.choice('ACGT') for _ in range(length))


def text_to_binary(text):
    """
    Converts a text message to binary representation.

    Parameters:
    - text (str): The input text message.

    Returns:
    - str: Binary representation of the input text.
    """
    binary_data = ''.join(format(ord(char), '08b') for char in text)
    return binary_data

def bytes_to_binary(data):
    """
    Converts a text message to binary representation.

    Parameters:
    - data (bytes): The input text message.

    Returns:
    - str: Binary representation of the input text.
    """
    binary_data = ''.join(format(char, '08b') for char in data)
    return binary_data