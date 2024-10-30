picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
]
for n1 in picture:
    for n2 in n1:
        if n2 == 0:
            print(" ", end="")
        else:
            print("*", end='')
    print("")
    # print("\n", end='')
