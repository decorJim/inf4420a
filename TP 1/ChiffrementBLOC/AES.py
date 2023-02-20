#!/usr/bin/env python3
import os
import argparse
from PIL import Image
from Crypto.Cipher import AES
from Crypto import Random

def main():
    """
    Ce script chiffre un fichier jpeg avec AES-256 en mode ECB ou CBC
    Options :
        -i, --input     fichier jpeg
        -m, --mode      ECB ou CBC
        -o, --out       fichier chiffre (facultatif)
    """
    # Handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="in_filename", required=True)
    parser.add_argument("-m", "--mode", dest="mode", choices=["ECB", "CBC"], required=True)
    parser.add_argument("-o", "--output", dest="out_filename")
    args = parser.parse_args()
    if not args.out_filename:
        fields = os.path.splitext(args.in_filename)
        args.out_filename = fields[0] + "_enc" + fields[1]
    if not os.path.exists(args.in_filename):
        print(f"[!] Input file {args.in_filename} not found, exiting")
        exit(1)

    # Generate keys
    key = Random.new().read(AES.key_size[2])
    iv = Random.new().read(AES.block_size)
    if args.mode == "ECB":
        cipher = AES.new(key, AES.MODE_ECB)
    else:
        cipher = AES.new(key, AES.MODE_CBC, iv)

    # Encrypt the image
    with Image.open(args.in_filename) as im:
        # Load all RGB pixels to a byte array
        data = list(im.getdata())
        nb_comp = len(data[0])
        data_array = b"".join([bytes(pixel) for pixel in data])

        print(len(data_array))
        # Pad the data to a multiple of 16
        nb_add = 0
        if len(data_array) % 16 != 0:
            nb_add = (16 - len(data_array) % 16)
            data_array += b"\x00" * nb_add

        data_array_enc = cipher.encrypt(data_array)

        # Reconstruct the pixel array
        data_array_enc = data_array_enc[:-nb_add]
        data_enc = [tuple(data_array_enc[i:i + nb_comp]) for i in range(0, len(data_array_enc), nb_comp)]

        # Save the encrypted image
        imNew = Image.new(im.mode, im.size)
        imNew.putdata(data_enc)
        imNew.save(args.out_filename)


if __name__ == '__main__':
    main()
