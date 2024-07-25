import crypto
with open("filter_crypto_russian.txt", "w", encoding="utf-8") as f:
    file = open("russian.txt", "r")
    word_list = file.read().split()
    censorship = ["говн", "сука", "падл", "хуй", "пизд", "бля", "ганд"]
    counter = 0
    for word in word_list:
        good_words = True
        for cens_word in censorship:
            if cens_word in word:
                print(word)
                good_words = False
                word_list.pop(counter)
                counter -= 1
                break

        if good_words:
            word = crypto.caesar_cipher_encrypt(word, crypto.crypt_word_numb)
            f.writelines(f"{word}\n")
        counter += 1
    file.close()
