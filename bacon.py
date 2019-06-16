import sys

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

vhid = sys.argv[1]
text = vhid.replace(" ", "")
if len(text)%5 != 0:
    text = text[:len(text) - (len(text)%5)]
n = len(text)
i = 5
list_1 = list(text)
list_1.insert(5, " ")

while i < n - 1:
    i += 6
    list_1.insert(i, " ")

for i in range(len(list_1)):
    if list_1[i].isalpha() and list_1[i].islower():
        list_1[i] = "a"
    elif list_1[i].isalpha() and list_1[i].isupper():
        list_1[i] = "b"
    else:
        list_1[i] = " "

if list_1[len(list_1) - 1] == " ":
    list_1.pop()

text_1 = "".join(list_1).replace(" ", "")
x = 0
text_uncr = ""
for j in range(int(n / 5)):
    y = key.find(text_1[x:x+5])
    text_uncr = text_uncr + alphabet[y]
    x += 5

print(text_uncr)