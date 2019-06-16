import sys

str = sys.argv[1].replace(' ','').lower()
str_back = str[::-1]
x = 0
for i in range(len(str)):
    if str[i] != str_back[i]:
        x+=1
        print("NO")
        break
if x == 0:
    print("YES")