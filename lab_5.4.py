list_1 = ['C:', 'backup.log', 'ideas.txt']
l1 = 'ideas.txt'
list_2 = [ 'D:', ['recycle bin'], ['tmp', ['old'], ['new folder1', 'asd.txt', 'asd.bak', 'find.me.bak' ] ], 'hey.py']
l2 = 'find.me'
list_3 = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
l3 = 'hereiam.py'

"""def file_search(folder, filename):

    link = 0"""

def file_search(folder, filename):

    route_search = str(folder[0]) + '/'

    if filename in folder[1:]:
        return route_search + filename

    else:
        for i in folder[1:]:
            if isinstance(i, str) == False and len(i) > 1:
                temp = file_search(i, filename)
                if temp != False:
                    route_search += str(temp)
                return route_search
    if route_search == route_search:
        return False
    else:
        return route_search

print(file_search(list_1, l1))
print(file_search(list_2, l2))
print(file_search(list_3, l3))