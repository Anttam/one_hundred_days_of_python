import pandas

df = pandas.read_csv('Day 26/nato_phonetic_alphabet.csv')
letters_dict = {}
coded_word = []
for (index, row) in df.iterrows():
  letters_dict.update({row.letter : row.code})

word = input('Enter the word you would like to encode: ').upper()
for letter in word:
  coded_word.append(letters_dict[letter])
print(coded_word)

