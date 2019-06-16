import sys

x = sys.argv[1]


def encode_morze(text):

    morse_code = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--.."}

    def change(a):

        if a in morse_code:
            b = morse_code.get(a)
            letter_morze = ''
            for i in range(len(b)):
                if i != len(b) - 1:
                    if b[i] == '.':
                        letter_morze += '^_'
                    else:
                        letter_morze += '^^^_'
                else:
                    if b[i] == '.':
                        letter_morze += '^'
                    else:
                        letter_morze += '^^^'
        else:
            letter_morze = ''

        return letter_morze


    n_list_n = text.upper().split()
    n_list = []
    for i in range(len(n_list_n)):
        word = ''
        for j in range(len(n_list_n[i])):
            if n_list_n[i][j].isalpha():
                word += n_list_n[i][j]
        n_list.append(word)

    sentences = ''

    for i in range(len(n_list)):
        for j in range(len(n_list[i])):
            if n_list[i][j].isalpha():
                sentences += change(n_list[i][j])
                if j != len(n_list[i]) - 1 and n_list[i][j + 1].isalpha():
                    sentences += '___'

        if i != len(n_list) - 1:
            x = 0
            for k in range(len(n_list[i])):
                if n_list[i][k].isalpha():
                    x += 1
            if x > 0:
                sentences += '_______'


    return sentences



print(encode_morze(x))
