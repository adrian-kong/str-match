def z_alg(text: str) -> []:
    # we ignore the first Z index, would be just |text|, no need to compute
    length = len(text) - 1
    z_arr = [0] * length
    l_tmp, r_tmp = 0, 0

    for i in range(1, length + 1):
        if i >= r_tmp:
            # simple iter O(n^2) basically, would function without the l_tmp, r_tmp caching
            for j in range(length - i + 1):
                if text[i + j] != text[j]:
                    break
                z_arr[i - 1] += 1
            l_tmp = i
            r_tmp = i + z_arr[i - 1]
        elif text[i] == text[0]:  # ith position == relative ith position
            rel_z = z_arr[i - l_tmp - 1]
            if i + rel_z >= r_tmp:
                excess = length - r_tmp + 1
                z_arr[i - 1] = r_tmp - i
                for j in range(excess):
                    if r_tmp + j > length or text[r_tmp + j] != text[r_tmp - i + j]:
                        break
                    z_arr[i - 1] += 1
                r_tmp = i + z_arr[i - 1]
                l_tmp = i
            else:
                z_arr[i - 1] = rel_z
    return z_arr
