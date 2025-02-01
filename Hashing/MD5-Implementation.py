import hashlib

# Function to generate MD5 hash of a given string
def generate_md5_hash(data):
    md5_hash = hashlib.md5()  # Create MD5 hash object
    md5_hash.update(data.encode('utf-8'))  # Update with data in byte format
    return md5_hash.hexdigest()  # Return the hexadecimal digest

data = "Hello, World!"
hash_result = generate_md5_hash(data)
print(f"MD5 Hash of '{data}': {hash_result}")
