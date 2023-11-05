from Elgamel import *


class EncodingScheme():

    def __init__(self):
        self.prime = generate_prime()
        self.prim_root = generate_prim_root(self.prime)

        keys = elgamel_key_creation(self.prime, self.prim_root)
        self.public_key = keys[0][2]
        self.private_key = keys[1]

    def convert_to_ascii(self, message):
        ascii_list = []
        for char in message:
            ascii_list.append(ord(char))
        return ascii_list

    def convert_to_string(self, ascii_list):
        message = ""
        for int_char in ascii_list:
            message += chr(int_char)
        return message

    def encrypt_el_gamel(self, message):
        ascii_list = self.convert_to_ascii(message)

        encrypted = []
        for char in ascii_list:
            encrypted.append(elgamel_encryption(self.prime, self.prim_root, self.public_key, char))
        return encrypted

    def decrypt_el_gamel(self, ciphertext):
        decrypted = []
        for char in ciphertext:
            decrypted.append(elgamel_decryption(char[0], char[1], self.prime, self.private_key))
        return self.convert_to_string(decrypted)

if __name__ == '__main__':
    message = "Hello"
    encoder = EncodingScheme()

    encryptedd = encoder.encrypt_el_gamel(message)
    print(f"Encrypted message {encryptedd}")
    decryptedd = encoder.decrypt_el_gamel(encryptedd)
    print(f"Decrypted message {decryptedd}")
