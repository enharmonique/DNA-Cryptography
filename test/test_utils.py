from utilities.utils import generate_random_dna_sequence, text_to_binary


def test_generate_random_dna_sequence():
    # Test if the generated DNA sequence has the correct length
    length = 10
    random_dna = generate_random_dna_sequence(length)
    assert len(random_dna) == length


def test_text_to_binary():
    # Test if the text is correctly converted to binary
    text1 = 'SECRET'
    binary_data1 = text_to_binary(text1)
    expected_binary_data1 = '010100110100010101000011010100100100010101010100'
    assert binary_data1 == expected_binary_data1

    text2 = 'Hello!'
    binary_data2 = text_to_binary(text2)
    expected_binary_data2 = '010010000110010101101100011011000110111100100001'
    assert binary_data2 == expected_binary_data2
