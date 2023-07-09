import os
import sys
import subprocess
import argparse
import random
import time
import marshal
import lzma
import gzip
import bz2
import binascii
import zlib
import string
import re
import keyword
import random
import colorama
import pyfiglet
import tqdm

# credits to thief cat for this obfuscator

def prett(text):
    return text.title().center(os.get_terminal_size().columns)
try:
    import tqdm
    import colorama
    import pyfiglet
except ModuleNotFoundError:
    if os.name == 'nt':
        _ = 'python'
    else:
        _ = 'python' + '.'.join(str(i) for i in sys.version_info[:2])
BLU = colorama.Style.BRIGHT + colorama.Fore.BLUE
CYA = colorama.Style.BRIGHT + colorama.Fore.CYAN
GRE = colorama.Style.BRIGHT + colorama.Fore.GREEN
YEL = colorama.Style.BRIGHT + colorama.Fore.YELLOW
RED = colorama.Style.BRIGHT + colorama.Fore.RED
MAG = colorama.Style.BRIGHT + colorama.Fore.MAGENTA
LIYEL = colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX
LIRED = colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX
LIMAG = colorama.Style.BRIGHT + colorama.Fore.LIGHTMAGENTA_EX
LIBLU = colorama.Style.BRIGHT + colorama.Fore.LIGHTBLUE_EX
LICYA = colorama.Style.BRIGHT + colorama.Fore.LIGHTCYAN_EX
LIGRE = colorama.Style.BRIGHT + colorama.Fore.LIGHTGREEN_EX
CLEAR = 'cls' if os.name == 'nt' else 'clear'
COLORS = BLU, CYA, GRE, YEL, RED, MAG, LIYEL, LIRED, LIMAG, LIBLU, LICYA, LIGRE
FONTS = 'basic', 'o8', 'cosmic', 'graffiti', 'chunky', 'epic', 'poison', 'doom', 'avatar'
PYTHON_VERSION = 'python' + '.'.join(str(i) for i in sys.version_info[:2])
colorama.init(autoreset=True)



def generate_random_name():
    length = random.randint(8, 15)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def is_valid_identifier(name):
    return name.isidentifier() and not keyword.iskeyword(name)

def obfuscate_code(source_code:str, whitelist:list) -> str:
    function_names = set(re.findall(r'def\s+(\w+)', source_code))
    user_function_names = [name for name in function_names if is_valid_identifier(name) and name not in whitelist]

    for function_name in user_function_names:
        new_name = generate_random_name()
        source_code = re.sub(r'\b{}\b'.format(function_name), new_name, source_code)
    obfuscated_code = source_code

    return obfuscated_code



def encode(source:str) -> str:
    selected_mode = random.choice((lzma, gzip, bz2, binascii, zlib))
    marshal_encoded = marshal.dumps(compile(source, 'Hornet', 'exec'))
    if selected_mode is binascii:
        encoded = binascii.b2a_base64(marshal_encoded)
    else:
        encoded = selected_mode.compress(marshal_encoded)
    if selected_mode is binascii:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads(binascii.a2b_base64({})))'
        return TMP.format(encoded)
    else:
        TMP = 'import marshal,lzma,gzip,bz2,binascii,zlib;exec(marshal.loads({}.decompress({})))'
        return TMP.format(selected_mode.__name__, encoded)

def logo() -> None:
    os.system(CLEAR)
    font = random.choice(FONTS)
    color1 = random.choice(COLORS)
    color2 = random.choice(COLORS)
    while color1 == color2:
        color2 = random.choice(COLORS)

def parse_args():
    parser = argparse.ArgumentParser(description='obfuscate python programs'.title())
    parser._optionals.title = "syntax".title()
    parser.add_argument(
        '-r','--recursion',
        default=False,
        required=False,
        help="recursion encoding by using this flag you will get x2 obfuscation strength".title(),
        dest='r',
        action='store_true')
    parser.add_argument('-i', '--input', type=str, help='input file name'.title(), required=True)
    parser.add_argument('-o', '--output', type=str, help='output file name'.title(), required=True)
    parser.add_argument('-s', '--strength', type=int,
                        help='strengthness of obfuscation. 100 recomended'.title(), required=True)
    if len(sys.argv)==1:
        exit()
    return parser.parse_args()





def main():
    args = parse_args()
    with tqdm.tqdm(total=args.strength) as pbar:
        with open(args.input) as input:
            whitelist = ['decode', 'run', 'start', 'replace', 'encode', '__main__', '__init__']
            input1 = obfuscate_code(input.read(), whitelist)
            if args.r:
                for i in range(args.strength):
                    if i == 0:
                        encoded = encode(source=input1)
                    else:
                        encoded = encode(source=encode(source=encoded))
                    time.sleep(0.1)
                    pbar.update(1)
            else:
                for i in range(args.strength):
                    if i == 0:
                        encoded = encode(source=input1)
                    else:
                        encoded = encode(source=encoded)
                    time.sleep(0.1)
                    pbar.update(1)
    with open(args.output, 'w') as output:
        output.write(f"import requests, json, socket, os, re, uuid, wmi, subprocess, winreg\n\ntry:\n\t{encoded}\nexcept KeyboardInterrupt:\n\tpass"
)
if __name__ == '__main__':
    logo()
    main()
