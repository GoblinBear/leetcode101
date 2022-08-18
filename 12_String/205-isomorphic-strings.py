def char_to_index(char):
        return ord(char) - ord('a')


def is_isomorphic(s, t):
    s_first_index = [0] * 26
    t_first_index = [0] * 26

    for i in range(len(s)):
        s_index = char_to_index(s[i])
        t_index = char_to_index(t[i])
        
        if s_first_index[s_index] != t_first_index[t_index]:
            return False
        
        s_first_index[s_index] = i + 1
        t_first_index[t_index] = i + 1

    return True


# Test
print(is_isomorphic("egg", "add"))
# Output: True
print(is_isomorphic("foo", "bar"))
# # Output: False
print(is_isomorphic("paper", "title"))
# # Output: True
