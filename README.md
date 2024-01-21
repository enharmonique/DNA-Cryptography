# DNA Cryptography Project

## Overview

This Python project demonstrates a simple DNA cryptography algorithm that encrypts and decrypts text messages using a substitution method. The algorithm converts binary data to a corresponding DNA sequence and vice versa.

## Algorithm

The algorithm involves the following steps:

1. **Text to Binary Conversion:**
   - The original text message is converted to binary using the `text_to_binary` function. Each character in the text is represented by its ASCII value in binary.

2. **DNA Encryption:**
   - The `encode_to_dna` function takes the binary data and a secret key as input.
   - It uses a substitution method to map each binary bit to a DNA base (AC or GT) based on random selections.
   - The random number generator is seeded with the secret key to ensure consistent results during encryption and decryption.

3. **DNA Decryption:**
   - The `decode_from_dna` function reverses the process, mapping each DNA base back to a binary bit.
   - The secret key is used to seed the random number generator for consistent decryption.

4. **Binary to Text Conversion:**
   - The final step involves converting the decrypted binary data back to a text message using ASCII values.
