# Information Security 🔐

This repository contains a collection of various cryptographic algorithms, key exchange protocols, and hashing functions, along with implementation examples of attacks and cryptanalysis techniques. The project is designed to explore different aspects of information security, focusing on classical ciphers, symmetric and asymmetric encryption, hashing, and attacks.

## Directory Structure 📂

    Information-Security
    │── README.md
    │── Crypto-Ciphers/
    │   ├── Classical-Ciphers/
    │   │   ├── Caesar-Cipher.py
    │   │   ├── Vigenere-Cipher.py
    │   │   ├── Playfair-Cipher.py
    │   ├── Symmetric-Ciphers/
    │   │   ├── DES-Implementation.py
    │   ├── Asymmetric-Ciphers/
    │   │   ├── RSA-Implementation.py
    │   │   ├── Diffie-Hellman-Key-Exchange.py
    │   ├── Hashing/
    │   │   ├── MD5-Implementation.py
    │   │   ├── SHA256-Implementation.py
    │   ├── Attacks/
    │   │   ├── BruteForce-Caesar.py

## Contents

### 1. **Classical Ciphers** 🏛️
This folder includes implementations of traditional cipher techniques:
- **Caesar Cipher**: A simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.
- **Vigenere Cipher**: A polyalphabetic substitution cipher that uses a keyword to encrypt the message.
- **Playfair Cipher**: A digraph cipher that encrypts pairs of letters using a 5x5 grid.

### 2. **Symmetric Ciphers**
Symmetric key algorithms use the same key for both encryption and decryption:
- **DES (Data Encryption Standard)**: A widely used symmetric-key block cipher for encrypting data.

### 3. **Asymmetric Ciphers**
Asymmetric encryption uses a public key for encryption and a private key for decryption:
- **RSA**: A widely used asymmetric encryption algorithm based on the mathematical properties of prime numbers.
- **Diffie-Hellman Key Exchange**: A method of securely exchanging cryptographic keys over a public channel.

### 4. **Hashing**
These files implement cryptographic hash functions, which are used to ensure data integrity:
- **MD5**: A widely known hashing algorithm, although considered weak due to vulnerabilities.
- **SHA-256**: A part of the SHA-2 family of cryptographic hash functions, more secure than MD5.

### 5. **Attacks**
This folder contains scripts that demonstrate cryptanalysis techniques:
- **BruteForce-Caesar**: A simple brute-force attack to decrypt Caesar cipher-encrypted text.

## Requirements

To run the Python implementations in this repository, you need the following libraries:
- Python 3.x
- No additional libraries are required for basic ciphers and hashing algorithms. For any advanced cryptographic protocols or attacks, you may need libraries such as `pycryptodome` for some implementations.

## How to Use

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your-username/Information-Security.git
    ```

2. Follow the script's prompts or check the comments in the code for instructions on how to input data and get results.

## Contributing

Feel free to fork the repository and submit pull requests if you wish to contribute improvements or additions, such as additional ciphers, cryptographic algorithms, or attacks.

