
def create_matrix(key):
    key = "".join(sorted(set(key), key=lambda x: key.index(x)))  # Remove duplicates and preserve order
    matrix = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # I and J share the same spot in the matrix

    for letter in alphabet:
        if letter not in key:
            key += letter  # Add the remaining letters of the alphabet to the key

    # Fill the 5x5 matrix
    for i in range(5):
        matrix.append(key[i * 5:(i + 1) * 5])

    return matrix


# preprocess text (remove spaces and handle 'J' as 'I')
def preprocess_text(text):
    text = text.replace(" ", "").upper()
    text = text.replace("J", "I")  # Treat 'J' as 'I' in Playfair Cipher

    # If the text length is odd, add an 'X' at the end
    if len(text) % 2 != 0:
        text += "X"

    return text


# Function to find position of a letter in the matrix
def get_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


# encrypt a pair of letters
def encrypt_pair(matrix, pair):
    row1, col1 = get_position(matrix, pair[0])
    row2, col2 = get_position(matrix, pair[1])

    if row1 == row2:  # Same row
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:  # Rectangle case
        return matrix[row1][col2] + matrix[row2][col1]

# decrypt a pair of letters
def decrypt_pair(matrix, pair):
    row1, col1 = get_position(matrix, pair[0])
    row2, col2 = get_position(matrix, pair[1])

    if row1 == row2:  # Same row
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:  # Same column
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:  # Rectangle case
        return matrix[row1][col2] + matrix[row2][col1]


def playfair(text, key, mode='encrypt'):
    matrix = create_matrix(key)
    text = preprocess_text(text)
    result = ""

    for i in range(0, len(text), 2):
        pair = text[i:i + 2]
        if mode == 'encrypt':
            result += encrypt_pair(matrix, pair)
        elif mode == 'decrypt':
            result += decrypt_pair(matrix, pair)

    return result


key = "KEYWORD"  # The key used for encryption
text = "HELLO"   #  message to be encrypted

encrypted_text = playfair(text, key, mode='encrypt')
decrypted_text = playfair(encrypted_text, key, mode='decrypt')

print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
