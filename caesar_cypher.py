alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class Encryptor:
    def __init__(self, tekst):
        self.tekst_2 = tekst

    def encryption(self):
        shift = int(input('podaj przesunięcie'))
        encrypted = ''
        for letter in self.tekst_2:
            if not(letter in alphabet):
                encrypted += letter
                continue
            position = alphabet.index(letter)
            new_pos = position + shift
            encrypted += alphabet[new_pos%26]
        self.tekst_2 = encrypted
        print(encrypted)

    def decryption(self):
        shift = int(input('podaj przesunięcie'))
        decrypted = ''
        for letter in self.tekst_2:
            if not (letter in alphabet):
                decrypted += letter
                continue
            position = alphabet.index(letter)
            new_pos = position - shift
            decrypted += alphabet[new_pos]
        self.tekst_2 = decrypted
        print(decrypted)


enigma = Encryptor(input('podaj wiadomość'))
enigma.encryption()
enigma.decryption()


