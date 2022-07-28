def naive(text: str) -> ([], int):
    length = len(text) - 1
    z_arr = [0] * length

    comps = 0  # counting comparisons

    for i in range(1, length + 1):
        for j in range(length - i + 1):
            comps += 1
            if text[i + j] != text[j]:
                break
            z_arr[i - 1] += 1

    return z_arr, comps
