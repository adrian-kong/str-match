def boyer_moore(txt: str, pat: str):
    z_arr = [0] * (len(pat) - 1)
    good_suffix = [0] * (len(pat) + 1)
    max_prefix = [0] * (len(pat))
    # can be array, but we take hashmap
    # to generalize input string
    R = {}
    # we dont care what ltmp is as long as its not initialized
    l_tmp, r_tmp = len(pat), len(pat)
    # pre-process pattern
    for i in range(len(pat) - 1, -1, -1):
        if not R.get(pat[i]):
            R[pat[i]] = i
        # pattern match offset, construct z table, skip the end since we know it will always be the full string
        if i != len(pat) - 1:
            if i < l_tmp:
                for j in range(i + 1):
                    if pat[- j - 1] != pat[i - j]:
                        break
                    z_arr[i] += 1
                l_tmp, r_tmp = i - z_arr[i], i
            elif pat[i] == pat[-1]:
                rel_z = z_arr[-r_tmp + i]
                if i - rel_z <= l_tmp + 1:
                    z_arr[i] = i - l_tmp
                    for j in range(len(pat)):
                        if l_tmp - j < 0 or pat[-r_tmp + l_tmp - j + 1] != pat[l_tmp - j]:
                            break
                        z_arr[i] += 1
                    l_tmp, r_tmp = i - z_arr[i], i
                else:
                    z_arr[i] = rel_z

            good_suffix[len(pat) - z_arr[i]] = max(good_suffix[len(pat) - z_arr[i]], i)

    print(good_suffix)
    # end preprocessing

    # start matching
    i = 0
    while i < (len(txt) - len(pat) + 1):
        for j in range(len(pat)):
            pat_index = len(pat) - j - 1
            if txt[i + pat_index] != pat[pat_index]:
                next_pos = R.get(txt[i + pat_index], -1)
                offset = 1
                if next_pos < pat_index:
                    offset = pat_index - next_pos
                gs = good_suffix[pat_index + 1]
                if gs > 0:
                    gs_offset = len(pat) - good_suffix[pat_index + 1] - 1
                    if gs_offset > offset:
                        offset = gs_offset
                i += offset
                break
        else:
            print(f"found pattern at {i}:{''.join([txt[i + k] for k in range(len(pat))])}")
            return i


boyer_moore("abcEabcFabc", "abcFabc")
