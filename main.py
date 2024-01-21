from dna_cryptography.encode_basic import encode_to_dna, decode_from_dna
from test.run_all_tests import run_all_tests
from utilities.utils import text_to_binary


def main():
    # Example text message and secret key
    text_message = 'Hello, DNA Cryptography!'
    secret_key = 'mysecretkey'

    # Convert text to binary
    binary_data = text_to_binary(text_message)

    # Encryption
    encrypted_dna = encode_to_dna(binary_data, secret_key)
    print(f'Original Text Message: {text_message}')
    print(f'Encrypted DNA Sequence: {encrypted_dna}')

    # Decryption
    decrypted_binary = decode_from_dna(encrypted_dna, secret_key)

    # Convert binary to text
    decrypted_text = ''.join([chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8)])

    print(f'Decrypted Text Message: {decrypted_text}')


if __name__ == "__main__":
    run_all_tests()
    main()
