import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row.letter: row.code for(index, row) in data.iterrows()}
# print(new_dict)


def nato():
    valid_word = True
    try:
        while valid_word:
            word = input("Enter a word: ").upper()
            output_list = [new_dict[letter] for letter in word]
            print(output_list)
            valid_word = False
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        nato()

nato()




