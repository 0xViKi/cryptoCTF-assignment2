from itertools import cycle, islice
import enchant
from sys import exit

def decrypt_vigenere_cipher(cipherText, vigenereKey):

    if len(cipherText) != len(vigenereKey):
       vigenereKey = ''.join(islice(cycle(vigenereKey), len(cipherText)))
    
    decryptedVigenerText = ""
    for c, k in zip(cipherText, vigenereKey):
        if c.islower():
            decryptedVigenerText += chr((ord(c) - ord(k) + 26) % 26 + ord('a'))
        elif c.isupper():
            decryptedVigenerText += chr((ord(c) - ord(k) + 26) % 26 + ord('A'))


    return decryptedVigenerText


def decrypt_rail_fence_cipher(cipherText, railNumber):
    # Create an empty matrix to mark the zigzag pattern
    rail = [['\n' for _ in range(len(cipherText))] for _ in range(railNumber)]
    
    # Step 1: Mark the zigzag pattern with '*'
    dir_down = None
    row, col = 0, 0
    
    for i in range(len(cipherText)):
        if row == 0:
            dir_down = True
        elif row == railNumber - 1:
            dir_down = False
        
        # Place a marker
        rail[row][col] = '*'
        col += 1

        row += 1 if dir_down else -1
    
    # Step 2: Fill the '*' positions with ciphertext characters
    index = 0
    for i in range(railNumber):
        for j in range(len(cipherText)):
            if rail[i][j] == '*' and index < len(cipherText):
                rail[i][j] = cipherText[index]
                index += 1

    # Step 3: Read the matrix in zigzag to construct plaintext
    result = []
    row, col = 0, 0
    dir_down = None

    for i in range(len(cipherText)):
        if row == 0:
            dir_down = True
        elif row == railNumber - 1:
            dir_down = False

        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1

        row += 1 if dir_down else -1

    return ''.join(result)


def decrypt_affine_cipher(ciphertext, affineKeyA, affineKeyB):
    alphabetLength = 26  # Alphabet size
    aInverse = pow(affineKeyA, -1, alphabetLength)
    plaintext = []

    for char in ciphertext:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            char = ord(char) - offset
            numericValue = (aInverse * (char - affineKeyB)) % alphabetLength
            plaintext.append(chr(numericValue + offset))
        else:
            plaintext.append(char)  # Preserve spaces, punctuation, etc.

    return ''.join(plaintext)


def decrypt_caesar_cipher(cipherText, caesarKey):

    plaintext = []

    for char in cipherText:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - offset - caesarKey) % 26 + offset)
            
            plaintext.append(decrypted_char)
        else:
            plaintext.append(char)  # Preserve spaces and punctuation

    return ''.join(plaintext)


def return_flag(fourWordString):

    dictionary = enchant.Dict("en_US")

    fourWordStringLength = len(fourWordString)
    dp = [None] * (fourWordStringLength + 1)
    dp[0] = []

    for i in range(1, fourWordStringLength + 1):
        for j in range(i):
            word = fourWordString[j:i]
            if dp[j] is not None and dictionary.check(word):
                if dp[i] is None or len(dp[j]) + 1 < len(dp[i]):
                    dp[i] = dp[j] + [word]

    return "_".join(dp[-1])

def ascii_banner():
    banner = r"""
   ____                          _                ____   _____   _____        _      ____  
  / ___|  _ __   _   _   _ __   | |_    ___      / ___| |_   _| |  ___|      / \    |___ \ 
 | |     | '__| | | | | | '_ \  | __|  / _ \    | |       | |   | |_        / _ \     __) |
 | |___  | |    | |_| | | |_) | | |_  | (_) |   | |___    | |   |  _|      / ___ \   / __/ 
  \____| |_|     \__, | | .__/   \__|  \___/     \____|   |_|   |_|       /_/   \_\ |_____|
                 |___/  |_|                                                                
"""
    print('-'*100)
    print(banner)
    print('-'*100)
    print('\n')

def main():

    vigenereKey = "armageddon"
    railNumber = 4 
    affineKeyA = 7
    caesarKey = 11
    affineKeyB = 0

    ascii_banner()
    
    cipherText = input("Enter Cipher Text: ").strip() 
    if not cipherText.isalpha():
        input("Invalid cipher text. Press enter to exit...")
        exit(0)
    try:
        affineKeyB = int(input("Enter Your Student ID: ")[-1])
    except Exception as e:
        input("Invalid Student ID. Press enter to exit...")
        exit(0)

    decipheredVignereText = decrypt_vigenere_cipher(cipherText=cipherText, vigenereKey=vigenereKey)
    decipheredRailFenceText = decrypt_rail_fence_cipher(cipherText=decipheredVignereText, railNumber=railNumber)
    decipheredAffineText = decrypt_affine_cipher(ciphertext=decipheredRailFenceText, affineKeyA=affineKeyA, affineKeyB=affineKeyB)
    decipheredText = decrypt_caesar_cipher(cipherText=decipheredAffineText, caesarKey=caesarKey)
    flag = return_flag(fourWordString=decipheredText)

    print()
    print('-'*100)
    print()
    print(f"FLAG: flag{{{flag}}}")
    print()
    print('-'*100)
    input("Press enter to exit...")


    

if __name__ == "__main__":
    main()