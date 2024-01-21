import random


def encode_to_dna(binary_data, key):
    """
    Encode binary data into a DNA sequence using a substitution method.

    Parameters:
    - binary_data (str): Binary data to be encoded.
    - key (str): Secret key for seeding the random number generator.

    Returns:
    - str: Encoded DNA sequence.
    """
    # Seed the random number generator with the secret key
    random.seed(key)

    # Encode each bit of binary data into a DNA base
    dna_sequence = ""
    for bit in binary_data:
        if bit == '0':
            dna_sequence += random.choice('AC')
        elif bit == '1':
            dna_sequence += random.choice('GT')

    return dna_sequence


def decode_from_dna(dna_sequence, key):
    """
    Decode a DNA sequence back into binary data using a substitution method.

    Parameters:
    - dna_sequence (str): DNA sequence to be decoded.
    - key (str): Secret key for seeding the random number generator.

    Returns:
    - str: Decoded binary data.
    """
    # Seed the random number generator with the secret key
    random.seed(key)

    # Decode each DNA base into a binary bit
    binary_data = ""
    for base in dna_sequence:
        if base in 'AC':
            binary_data += '0'
        elif base in 'GT':
            binary_data += '1'

    return binary_data
