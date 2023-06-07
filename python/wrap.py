xlist = []
def wrap(string, max_width):
    xx = 0
    x = 0
    i = xx
    max_w = max_width
    while x < len(string):
        xlist.append(string[i:max_w])
        max_w += max_width
        i += max_width
        x += max_width
    string = '\n'.join(xlist)
    return string

print(wrap("azerqsdf", 2))