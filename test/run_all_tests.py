from test.test_utils import test_generate_random_dna_sequence, test_text_to_binary
from test.test_encryption import test_encode, test_encode_xor

def run_all_tests():
    test_generate_random_dna_sequence()
    test_text_to_binary()
    test_encode()
    test_encode_xor()
