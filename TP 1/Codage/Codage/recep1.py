#!/usr/bin/env python3
import sys
from Crypto.Cipher import DES

def main():
    """
    Ce script implemente le dechiffrement DES suivi du decodeur 1
    """

    if len(sys.argv) != 1:
        print("Erreur de syntaxe")
        print(main.__doc__)
        return 1

    ciphertext = sys.stdin.buffer.read(8)
    if len(ciphertext) != 8:
        print("Le texte chiffre doit avoir exactement 64 bits")
        return 2

    # Cle generee par Random.new().read(DES.key_size)
    key = b"\xe8\x8e\x0e\x16-\x88\xf6\x10"

    # IV genere par Random.new().read(DES.block_size)
    iv = b"\x9a=\xa7#+\x85\xf3\xab"

    cipher = DES.new(key, DES.MODE_CBC, iv)
    code = cipher.decrypt(ciphertext)
    
    # Extraction des 2 premiers octets
    pin_bin = bin(code[0])[2:].zfill(8) + bin(code[1])[2:].zfill(8)
    parity_chk = str(pin_bin[:7].count("1") % 2)
    parity_chk += str(pin_bin[7:14].count("1") % 2)

    if (pin_bin[-2:] != parity_chk):
        print("Erreur dans la transmission")
        return 4

    pin = int(pin_bin[:14], 2)
    sys.stdout.write(str(pin))


if __name__ == "__main__":
    main()
