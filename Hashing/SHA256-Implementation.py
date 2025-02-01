import hashlib

# Function to generate SHA256 hash of a given string
def generate_sha256_hash(data):
    sha256_hash = hashlib.sha256()  # Create SHA256 hash object
    sha256_hash.update(data.encode('utf-8'))  # Update with data in byte format
    return sha256_hash.hexdigest()  # Return the hexadecimal digest

# Example usage
data = "Hello, World!"
hash_result = generate_sha256_hash(data)
print(f"SHA256 Hash of '{data}': {hash_result}")
