def vigenere_cipher(text, key, encrypt=True):
    result = ""
    key = key.upper()
    key_length = len(key)
    key_index = 0
    
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - 65
            shift = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr(((ord(char) - ascii_offset + shift) % 26) + ascii_offset)
            key_index += 1
        else:
            result += char
    return result

if __name__ == "__main__":
    plaintext = "HELLO KINZA"
    key = "CRYPTO"
    
    encrypted_text = vigenere_cipher(plaintext, key)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = vigenere_cipher(encrypted_text, key, encrypt=False)
    print(f"Decrypted: {decrypted_text}")