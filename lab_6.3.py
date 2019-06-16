
list_in = [[1,2,3],[3,2,1]]
list_in_1 = [[8,3,0,1,2,3,4,8,1,2,3],[3,2,1,2,3,9,4,7,9,2,3],[7,6,0,1,3,5,2,3,4,1,1]]
list_in_2 = [[21]]
list_in_3 = [[1,2,3,0,1,1], [4,3,2,1,1,2], [4,3,2,0,1,1], [0,0,0,0,0,1]]
list_in_4 = [[5,5,5], [5,5,6], [5,4,5]]
list_in_5 = [[3,5,1]]


def saddle_point(matrix):
    i_1 = -1
    i_2 = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            list_temp = []
            if matrix[i][j] == min(matrix[i]) and matrix[i].count(min(matrix[i])) == 1:
                for k in range(len(matrix)):
                    list_temp.append(matrix[k][j])
                if matrix[i][j] == max(list_temp) and list_temp.count(max(list_temp)) == 1:
                    i_1 = i
                    i_2 = j
    if i_1 == -1:
        return False
    else:
        return (i_1, i_2)


print(saddle_point(list_in))
print(saddle_point(list_in_1))
print(saddle_point(list_in_2))
print(saddle_point(list_in_3))
print(saddle_point(list_in_4))
print(saddle_point(list_in_5))

