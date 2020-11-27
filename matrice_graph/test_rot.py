def rotate(state, id, isRow):
    rowOrCol = [0, 0, 0]
    temp = 0
    if isRow:
        rowOrCol = state[id]
        temp = rowOrCol[0]
        for i in range(2):
            rowOrCol[i] = rowOrCol[i + 1]
        rowOrCol[2] = temp
        state[id] = rowOrCol
    else:
        for i in range(3):
            rowOrCol[i] = state[i][id]
        temp = rowOrCol[0]
        for j in range(2):
            rowOrCol[j] = rowOrCol[j + 1]
        rowOrCol[2] = temp
        for k in range(3):
            state[k][id] = rowOrCol[k]
    return


def main():
    state = [[1, 1, 0], [1, 1, 0], [0, 1, 1]]

    for i in range(3):
        rotate(state, i, True)

    print(state)

    for j in range(3):
        rotate(state, j, False)

    print(state)

    state = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    rotate(state, 2, True)
    rotate(state, 2, True)
    rotate(state, 2, True)
    print(state)


if __name__ == '__main__':
    main()
