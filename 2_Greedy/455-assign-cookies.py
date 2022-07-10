def find_content_children(g, s):
    children = sorted(g)
    cookies = sorted(s)

    child = 0
    cookie = 0

    while child < len(children) and cookie < len(cookies):
        if children[child] <= cookies[cookie]:
            child = child + 1
        cookie = cookie + 1

    return child


# Test
print(find_content_children([1, 2, 3], [1, 1]))
print(find_content_children([1, 2], [1, 2, 3]))
