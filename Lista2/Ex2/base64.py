import argparse
from textwrap import wrap

arr = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

def encode(txt, out = 'encoded.txt'):
    with open(txt, 'r') as input_file:
        txt = input_file.read()
    str_to_binary = ''.join((8 - len(format(ord(letter), 'b'))) * '0' + format(ord(letter), 'b') for letter in txt)
    splitted_bin = wrap(str_to_binary, 6)
    shift = int((6 - len(splitted_bin[len(splitted_bin)-1]))/2)
    splitted_bin[len(splitted_bin)-1] += (shift*2) * '0'
    encoded_txt = ''
    for element in splitted_bin:
        encoded_txt += arr[int(element, 2)]
    encoded_txt += shift * '='
    with open(out, 'w') as output_file:
        output_file.write(encoded_txt)


def decode(txt, out = 'decoded.txt'):
    with open(txt, 'r') as input_file:
        txt = input_file.read()
    shift = txt.count('=')
    txt_without_shifting = txt[:(-shift)]
    binary_representation = ''
    for char in txt_without_shifting:
        binary_representation += (6 - len((str(bin(arr.index(char)))[2:]))) * '0' + str(bin(arr.index(char)))[2:]
    binary_representation = binary_representation[:-(2*shift)]
    list_to_decode = wrap(binary_representation, 8)
    decoded_str = ''
    for element in list_to_decode:
        decoded_str += chr(int(element,2))
    with open(out, 'w') as output_file:
        output_file.write(decoded_str)


parser = argparse.ArgumentParser()
parser.add_argument("--encode", action='count', default=0)
parser.add_argument('--decode', action='count', default=0)
parser.add_argument('x')
parser.add_argument('y')
args = parser.parse_args()
if args.encode:
    encode(args.x, args.y)
elif args.decode:
    decode(args.x, args.y)

