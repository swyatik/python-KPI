
def make_sudoku(size):
    matrix = [[0] * (size ** 2) for i in range(size ** 2)]
    step = 0
    step_size = 1
    for i in range(size ** 2):
        if i % size == 0 and step != 0:
            step = step_size
            step_size += 1
        elif step == 0:
            step = 0
        else:
            step = step + size
        for j in range(size ** 2):
            if step >= size ** 2:
                step = step + 1 - (size ** 2)
                matrix[i][j] = step
            else:
                step += 1
                matrix[i][j] = step
    return matrix



def output_matrix(mat):
    for row in mat:
        string = ''
        for el in row:
            string = string + "%4d" % (el)
        print(string)


print(make_sudoku(42))
print('-----------------------------------------------------------------------------')
a1 = make_sudoku(42)
output_matrix(a1)