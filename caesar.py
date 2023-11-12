def caesar_decrypt(cipher_text, shift):
    result = ''

    for char in cipher_text:
        if char == ' ':
            result += ' '
        else:
            char_code = ord(char) - shift
            if char_code < 65:
                char_code += 26
            result += chr(char_code)

    return result

# Contoh penggunaan:
cipher_text = "ELANDA RIK M"
shift = 1
decrypted_text = caesar_decrypt(cipher_text, shift)

print(f"Teks Terenkripsi: {cipher_text}")
print(f"Hasil Dekripsi: {decrypted_text}")
