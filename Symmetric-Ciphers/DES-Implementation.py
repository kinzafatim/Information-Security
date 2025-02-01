from pyDes import des, CBC, PAD_PKCS5

key = b"abcdefgh"  # 8-byte key (must be 8 bytes for DES)
data = b"Hello, World!"  # Data to encrypt

# Initialize DES cipher
cipher = des(key, CBC, IV=b"12345678", pad=None, padmode=PAD_PKCS5)

encrypted_data = cipher.encrypt(data)
print(f"Encrypted: {encrypted_data}")


decrypted_data = cipher.decrypt(encrypted_data)
print(f"Decrypted: {decrypted_data.decode()}")

