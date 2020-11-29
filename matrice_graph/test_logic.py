"""
Test script for business logic.
"""


def get_state(cell_id):
    state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    binary = '{0:09b}'.format(cell_id)
    index = 0
    for char in binary:
        state[index // 3][index % 3] = int(char)
        index += 1
    return state


def get_id(state):
    cell_id = 0
    exponent = 8
    for row in state:
        for column in row:
            if column == 1:
                cell_id += pow(2, exponent)
            exponent -= 1
    return cell_id


def invert(state, row, col):
    if state[row][col] == 1:
        state[row][col] = 0
    else:
        state[row][col] = 1
    return


def main():
    numbers = [0, 1, 2, 4, 8, 16, 32, 64, 128, 256]
    numbers2 = [1, 3, 7, 15, 31, 63, 127, 255, 511]

    # for i in numbers:
    #    print(i)
    #    print(getState(i))
    #    print(getId(getState(i)))

    # for j in numbers2:
    #    print(j)
    #    print(getState(j))
    #    print(getId(getState(j)))

    state1 = get_state(0)

    # neighbours with inverting rows
    for j in range(3):
        state2 = state1
        for k in range(3):
            invert(state2, j, k)
        print(state1)
        print(state2)
        neighbour_id = get_id(state2)
        print("Joining", get_id(state1), " and ", get_id(state2))


if __name__ == '__main__':
    main()
