#!/usr/bin/env python3
import sys
from Crypto.Cipher import DES

def main():
    """
    Ce script implemente le dechiffrement DES suivi du decodeur de base
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
    code = cipher.decrypt(ciphertext).decode()

    if not(code.isdigit()):
        print("Erreur le texte chiffre est incorrect")
        return 3

    if (code[:4] != code [4:8]):
        print("Erreur dans la transmission")
        return 4

    sys.stdout.write(code[:4])


if __name__ == "__main__":
    main()
