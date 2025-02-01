
def caesar_bruteforce(ciphertext):
    for shift in range(1, 26):
        decrypted_text = ''
        for char in ciphertext:
            if char.isalpha():
                shift_amount = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
            else:
                decrypted_text += char
        print(f"Shift {shift}: {decrypted_text}")

ciphertext = "Uifsf jt b tfdsfu dpef!"  # "There is a secret code!" with Caesar cipher
print("Brute Force Caesar Cipher Decryptions:")
caesar_bruteforce(ciphertext)
