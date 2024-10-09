text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. "
        "Integer urna nisl, facilisis vitae semper at, dignissim vitae libero")
punctuation_marks_one_symbol = (',', '.', '!', '?', ';')
punctuation_marks_three_symbols = ('!!!', '...', '???')
words = text.split()
final_text = []

for word in words:
    if word.endswith(punctuation_marks_one_symbol):
        punctuation_mark = word[:-2:-1]
        # final_word = word.rstrip(punctuation_mark) + 'ing' + punctuation_mark  # +
        final_word = ''.join([word.strip(punctuation_mark), 'ing', punctuation_mark])  # join
        final_text.append(final_word)
    elif word.endswith(punctuation_marks_three_symbols):
        punctuation_mark = word[:-4:-1]
        # final_word = word.rstrip(punctuation_mark) + 'ing' + punctuation_mark  # +
        final_word = ''.join([word.rstrip(punctuation_mark), 'ing', punctuation_mark])  # join
        final_text.append(final_word)
    else:
        # final_word = word + 'ing'  # +
        final_word = ''.join([word, 'ing'])  # join
        final_text.append(final_word)

print(' '.join(final_text))
