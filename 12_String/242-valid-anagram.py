def char_to_index(char):
        return ord(char) - ord('a')


def is_anagram(s: str, t: str):
    s_size = len(s)
    t_size = len(t)

    if s_size != t_size:
        return False

    counts = [0] * 26
    for i in range(s_size):
        s_index = char_to_index(s[i])
        counts[s_index] = counts[s_index] + 1
        t_index = char_to_index(t[i])
        counts[t_index] = counts[t_index] - 1

    for count in counts:
        if count != 0:
            return False
    
    return True


# Test
print(is_anagram("anagram", "nagaram"))
# Output: True
print(is_anagram("rat", "car"))
# Output: False
