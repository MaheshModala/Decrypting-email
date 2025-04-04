def decrypt_substitution_cipher(ciphertext):
    substitution_map = {
        'h': 't',
        'u': 'h',
        'q': 'e',
        's': 'r',
        'r': 'i',
        'y': 's',
        'e': 'm',
        'l': 'a',
        'b': 'n',
        'f': 'y',
        'k': 'o',
        'g': 'u',
        'c': 'c',
        'm': 'd',
        'x': 'l',
        'z': 'w',
        'a': 'b',
        'v': 'f',
        't': 'g',
        'n': 'd',
        'o': 'p',
        'w': 'v',
        'd': 'e',
        'j': 'j',
        'i': 'a',
        'p': 's'
    }
    
    # Convert the ciphertext to lowercase
    ciphertext = ciphertext.lower()
    
    # Apply the substitution map
    plaintext = ""
    for char in ciphertext:
        if char in substitution_map:
            plaintext += substitution_map[char]
        else:
            plaintext += char
            
    return plaintext

# Testing
ciphertext = """huqsqryelbflfkgbtckcmqsqxhulhzrxxyhlbngokblngbturxxlbncskzlakghuryvlhuqsafzlfkvelmrbturykzboxgeltqhkyurbqbqwqsvkstqhzulhfkglsqvksygsqxfhuqzksxnzrxxbkhelmqrhfkgsyhsqbthuhuqbrhclbbqwqsaqfkgszqlmbqyylseksfkgsyqxvrbrhlbnrhzrxxbqwqsaqgyqnhkugshfkgafhuryuqyqqeqnhkeqlbbkhkbxfhulhhuqekyhsqxrlaxqlbngyqvgxckgsltqzlyhulhzurculsryqyvskehuqvlrsqyhrelhrkbkvhuqqbckgbhqsqnoqsrxaghhulhlbghhqsxfvqlsxqyyelbrylvlseksqnlbtqskgyckeslnqhulblckzlsnfkgzrxxoskvrhafhuqvlrxgsqlbnzrxxlwkrnrhlbkhuqshreqrulwqnkbqlyrerxlshurbtefyqxvrbckbyhsgchrkbkvhqbqwqsfvlrxgsqhqlcuqylelbykeqhurbtrvuqzrxxxqlsbukbqyhoqkoxqnkbhurnqhuqrsnqqny"""

plaintext = decrypt_substitution_cipher(ciphertext)
print(plaintext)
