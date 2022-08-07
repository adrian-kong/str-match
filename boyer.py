def boyer_moore(text: str):
    length = len(text) - 1
    z_arr = [0] * length

    for i in range(0, length):
        print()