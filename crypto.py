import random


def caesar_cipher_encrypt(plaintext, shift = 7):
  """
  Шифрует строку с использованием шифра Цезаря.

  Args:
    plaintext: Исходная строка (строка).
    shift: Смещение для шифрования (целое число).

  Returns:
    Зашифрованная строка (строка).
  """
  ciphertext = ""
  i = 0
  if shift != 7:
      salt = "Арсюха гений он настолько гениален что у него пса зовут вафел"
      crypto_salt = caesar_cipher_encrypt(salt)

  for char in plaintext:
    if char.isalpha():
      char_code = ord(char)

      if char.islower():
        char_code += shift
        char_code = ((char_code - ord("а")) % 33) + ord("а")
      else:
        char_code += shift
        char_code = ((char_code - ord("А")) % 33) + ord("А")

      char = chr(char_code)

    else:
      char = char
    ciphertext += char
    i += 1
    if shift != 7:
        for j in range(2):
            ciphertext += crypto_salt[i + j]
  return ciphertext

def caesar_cipher_deencrypt(plaintext, shift):
  """
  Дешифрует строку с использованием шифра Цезаря.

  Args:
    plaintext: Исходная строка (строка).
    shift: Смещение для шифрования (целое число).

  Returns:
    Зашифрованная строка (строка).
  """
  ciphertext = ""
  answer = ""
  for k in range(0, len(plaintext), 3):
    answer += plaintext[k]
  for char in answer:
    if char.isalpha():
      char_code = ord(char)

      if char.islower():
        char_code += shift
        char_code = ((char_code - ord("а")) % 33) + ord("а")
      else:
        char_code += shift
        char_code = ((char_code - ord("А")) % 33) + ord("А")

      char = chr(char_code)

    else:
      char = char
    ciphertext += char
  return ciphertext

word_word = "Слово"
crypt_word_numb = 1245
"""
crypto_word = caesar_cipher_encrypt(word_word, crypt_word_numb)
print(crypto_word)
answer = ""
print(caesar_cipher_deencrypt(crypto_word, -crypt_word_numb))

file = open("filter_crypto_russian.txt", "r", encoding="utf-8")
word_list = file.readlines()
password = caesar_cipher_deencrypt(word_list[random.randint(0, len(word_list))], -crypt_word_numb)
print(password)
file.close()
"""