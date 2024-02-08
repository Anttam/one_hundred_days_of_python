import pandas

df = pandas.read_csv('Day 26/nato_phonetic_alphabet.csv')

letters_dict = {row.letter: row.code for (index, row) in df.iterrows()}

word = input('Enter the word you would like to encode: ').upper()

coded_word = [letters_dict[letter] for letter in word]

print(coded_word)

