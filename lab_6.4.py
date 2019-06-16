
tex = 'Hello,Hello, my dear!'
xex = ''
lex = 'Mom! Mom! Are,mom-mom-m-mom you sleeping?!!!'
fex = 'to understand recursion you need first to understand recursion...'

def find_most_frequent(text):
    if text == '':
        return []
    else:
        t = ''
        for i in range(len(text)):
            if text[i].isalpha():
               t += text[i].lower()
            else:
                t += ' '
        text_list = t.split()
        text_search = list(set(text_list))
        sentences_count = []

        for i in range(len(text_search)):
            sentences_count.append(text_list.count(text_search[i]))

        max_count = max(sentences_count)
        list_out = []

        if sentences_count.count(max_count) > 1:
            for i in range(len(sentences_count)):
                if max_count == sentences_count[i]:
                    list_out.append(text_search[i])
            list_out.sort()
        else:
            list_out.append(text_search[sentences_count.index(max_count)])

        return list_out


print(find_most_frequent(tex))
print(find_most_frequent(lex))
print(find_most_frequent(xex))
print(find_most_frequent(fex))

