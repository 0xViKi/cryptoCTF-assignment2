# Crypto CTF Assignment 2 Challenge Solver

A Python-based cryptography challenge solver that decrypts multiple encryption layers to recover a secret flag.

## Overview

This program decrypts a cipher text that has been encrypted with multiple classical cryptographic algorithms in sequence:

1. Caesar cipher
2. Affine cipher
3. Rail fence cipher
4. Vigenère cipher

After successful decryption, the program parses the plaintext into meaningful words and constructs a flag.

## Features

- Multiple encryption layer decryption
- Implementation of four classical cryptographic algorithms
- Automatic word segmentation and flag generation
- ASCII banner visualization

## Requirements

- Python 3.x
- PyEnchant library (for dictionary word checking)

## Installation

1. Clone this repository
```bash
git clone https://github.com/0xViKi/cryptoCTF-assignment2.git
cd cryptoCTF-assignment2
```

2. Install required dependencies
```bash
pip install pyenchant
```

## Usage

Run the script:
```bash
python crypto-ctf2.py
```

When prompted:
1. Enter the cipher text (alphabetic characters only)
2. Enter your Student ID (the last digit will be used as the Affine cipher's B value)

The program will:
- Decrypt the text through all layers
- Identify words in the plaintext
- Generate and display the flag

## How It Works

### Decryption Process

The program applies the following decryption steps in sequence:

1. **Vigenère Cipher** decryption with the key "armageddon"
2. **Rail Fence Cipher** decryption with 4 rails
3. **Affine Cipher** decryption with parameters A=7 and B=(last digit of student ID)
4. **Caesar Cipher** decryption with a shift of 11

### Flag Generation

After decryption, the plaintext is parsed into English words using PyEnchant. These words are joined with underscores to form the flag format: `flag{word1_word2_word3_word4}`.

## Example

```
----------------------------------------------------------------------------------------------------
   ____                          _                ____   _____   _____        _      ____  
  / ___|  _ __   _   _   _ __   | |_    ___      / ___| |_   _| |  ___|      / \    |___ \ 
 | |     | '__| | | | | | '_ \  | __|  / _ \    | |       | |   | |_        / _ \     __) |
 | |___  | |    | |_| | | |_) | | |_  | (_) |   | |___    | |   |  _|      / ___ \   / __/ 
  \____| |_|     \__, | | .__/   \__|  \___/     \____|   |_|   |_|       /_/   \_\ |_____|
                 |___/  |_|                                                                
----------------------------------------------------------------------------------------------------

Enter Cipher Text: ABCDEFGHIJKLMNOP
Enter Your Student ID: 123456789

----------------------------------------------------------------------------------------------------

FLAG: flag{example_decrypted_words_here}

----------------------------------------------------------------------------------------------------
```

## Cryptographic Algorithms

### Vigenère Cipher
A polyalphabetic substitution cipher that uses a keyword to determine shifts.

### Rail Fence Cipher
A transposition cipher that writes plaintext in a zigzag pattern along a set number of "rails" and reads off by row.

### Affine Cipher
A monoalphabetic substitution cipher that uses the function (ax + b) mod 26 for encryption.

### Caesar Cipher
A substitution cipher where each letter is shifted by a fixed number of positions.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
