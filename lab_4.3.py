import sys

string = sys.argv[1]
x = string
while x.find("()") != -1:
        x = x.replace("()", "")
if x == "":
    print("YES")
else:
    print("NO")
