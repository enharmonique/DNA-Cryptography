from dna_cryptography.encode_basic import encode_to_dna, decode_from_dna
from dna_cryptography.encode_xor import encode_to_dna_xor, decode_from_dna_xor
from utils import text_to_binary


def _test_encodings(encode,decode):
    keys = ["test1", "secret_key", "hguyftosor89"]
    toEncode = ["message1", "Hello World!", "According to all known laws of aviation, there is no way that a bee should be able to fly. It's wings are too small to get it's fat little body off the ground. The bee, of course, flies anyways."] 
    for key in keys:
        for code in toEncode:
            code = text_to_binary(code)
            assert decode(encode(code,key),key) == code


def test_encode():
    _test_encodings(encode_to_dna,decode_from_dna)


def test_encode_xor():
    _test_encodings(encode_to_dna_xor,decode_from_dna_xor)
