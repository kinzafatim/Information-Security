import numpy as np

def mod_inverse(matrix, mod=26):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = pow(det, -1, mod)
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % mod
    return (det_inv * adj) % mod

def text_to_numbers(text):
    return [ord(char) - 65 for char in text.upper() if char.isalpha()]

def numbers_to_text(numbers):
    return "".join(chr(num + 65) for num in numbers)

def hill_cipher(text, key_matrix, encrypt=True):
    matrix = np.array(key_matrix)
    if not encrypt:
        matrix = mod_inverse(matrix)
    
    text_nums = text_to_numbers(text)
    if len(text_nums) % len(matrix) != 0:
        text_nums.extend([0] * (len(matrix) - len(text_nums) % len(matrix)))
    
    text_matrix = np.array(text_nums).reshape(-1, len(matrix))
    result_matrix = np.dot(text_matrix, matrix) % 26
    
    return numbers_to_text(result_matrix.flatten())

if __name__ == "__main__":
    plaintext = "HELP"
    key_matrix = [[6, 24], [1, 13]]
    
    encrypted_text = hill_cipher(plaintext, key_matrix)
    print(f"Encrypted: {encrypted_text}")
    
    decrypted_text = hill_cipher(encrypted_text, key_matrix, encrypt=False)
    print(f"Decrypted: {decrypted_text}")
