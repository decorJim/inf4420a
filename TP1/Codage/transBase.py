#!/usr/bin/env python3
import sys
from Crypto.Cipher import DES

def main():
    """
    Ce script implemente le codeur de base suivi du chiffrement DES
    Usage:
        python3 transBase.py NIP

    Le NIP doit avoir exactement 4 chiffres
    """

    if len(sys.argv) != 2:
        print("Erreur de syntaxe")
        print(main.__doc__)
        return 1

    pin = sys.argv[1]
    if len(pin) != 4 or not(pin.isdigit()):
        print("Le NIP doit avoir exactement 4 chiffres")
        return 2

    code = pin * 2

    # Cle generee par Random.new().read(DES.key_size)
    key = b"\xe8\x8e\x0e\x16-\x88\xf6\x10"

    # IV genere par Random.new().read(DES.block_size)
    iv = b"\x9a=\xa7#+\x85\xf3\xab"

    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(code.encode())
    sys.stdout.buffer.write(ciphertext)


if __name__ == "__main__":
    main()
