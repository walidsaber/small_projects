def swap_case(s):
    li = list(s)
    x = 0
    for i in li:
        if ord(i) >= 65 and ord(i) <= 90:
            li[x] = chr(ord(i) + 32)
        elif ord(i) >= 97 and ord(i) <= 122:
            li[x] = chr(ord(i) - 32)
        x += 1
    s = ''.join(li)
    return s

print(swap_case("SdserWalidSde \"reds 584 re avenue"))