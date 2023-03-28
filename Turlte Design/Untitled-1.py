# Define the substitution key as a dictionary
key = {
    'N': 'A', 'R': 'B', 'G': 'C', 'Z': 'D', 'T': 'E', 'Y': 'F', 'V': 'G', 'I': 'H', 
    'O': 'I', 'U': 'J', 'B': 'K', 'E': 'L', 'L': 'M', 'X': 'N', 'K': 'O', 'M': 'P', 
    'A': 'Q', 'F': 'R', 'D': 'S', 'P': 'T', 'H': 'U', 'C': 'V', 'S': 'W', 'Q': 'X', 
    'J': 'Y', 'W': 'Z'
}

# Define the encrypted message
encrypted_message = "Nrgzt rh kvi gsv ozmtzyvi lu zkkvi, rm z uziwrzhp svoozb, gsvh lu blfizgrlm xrksvi gsv yvtrgfiv gszg rh yovn. Gsv ozmtzyvi rh hfyhgrxzo gsv luvi dzhxibkz, zmw lfi hroo yvhhv lu yvxrg ziv gsv xovzhhv zmw fovyizgviv zmw wyvmtizh lu szev zkkvi."

# Define a function to decrypt the message
def decrypt_message(message):
    decrypted_message = ''
    for character in message:
        if character in key:
            decrypted_message += key[character]
        else:
            decrypted_message += character
    return decrypted_message

# Call the decrypt_message function with the encrypted message as the argument
decrypted_message = decrypt_message(encrypted_message)

# Print the decrypted message
print(decrypted_message)
