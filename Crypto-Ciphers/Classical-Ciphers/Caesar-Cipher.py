def caesar_cipher(text, shift, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift if encrypt else -shift
            ascii_offset = 65 if char.isupper() else 97
            result += chr(((ord(char) - ascii_offset + shift_amount) % 26) + ascii_offset)
        else:
            result += char
    return result

def brute_force_caesar(ciphertext):
    print("\nBrute Force Results:")
    for shift in range(26):
        decrypted_text = caesar_cipher(ciphertext, shift, encrypt=False)
        print(f"Shift {shift}: {decrypted_text}")

if __name__ == "__main__":
    plaintext = "HELLO KINZA"
    shift_key = 3
    
    encrypted_text = caesar_cipher(plaintext, shift_key)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = caesar_cipher(encrypted_text, shift_key, encrypt=False)
    print(f"Decrypted: {decrypted_text}")
    
    brute_force_caesar(encrypted_text)
