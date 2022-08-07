def naive(text: str) -> []:
    length = len(text) - 1
    z_arr = [0] * length

    for i in range(1, length + 1):
        for j in range(length - i + 1):
            if text[i + j] != text[j]:
                break
            z_arr[i - 1] += 1

    return z_arr
