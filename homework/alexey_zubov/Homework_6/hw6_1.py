text = "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, " \
    "facilisis vitae semper at, dignissim vitae libero"

words = text.split()
fin_words = []

for word in words:
    if word and not word[-1].isalpha():
        main_part = word[:-1]
        punctuation = word[-1]
        new_word = main_part + "ing" + punctuation
    else:
        new_word = word + "ing"

    fin_words.append(new_word)

result_text = " ".join(fin_words)
print(result_text)
