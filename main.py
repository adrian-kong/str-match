# str = "aabcaabxaay"
str = "aaabaaab"


def z_alg(text: str) -> []:
    length = len(text) - 1

    z_arr = [0] * length

    l_tmp, r_tmp, z_tmp = 0, 0, 0

    for i in range(1, length + 1):

        if r_tmp < i:
            z = 0
            for j in range(0, length - i + 1):
                if text[i + j] != text[j]:
                    break
                z += 1
            z_arr[i - 1] = z
            l_tmp, z_tmp = i, z
            r_tmp = l_tmp + z_tmp
        elif text[i] == text[i - l_tmp]:
            old_z = z_arr[i - l_tmp - 1]
            if i + old_z > r_tmp:
                excess = r_tmp - old_z - i
                for j in range(0, excess):
                    if text[r_tmp + j] != text[r_tmp - i + j]:
                        break
                    old_z += 1
            z_arr[i - 1] = old_z
    print(z_arr)

    return z_arr


z_alg(str)
