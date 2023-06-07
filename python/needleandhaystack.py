def strsstr(haystack, needle):
    #counts the number of times matching
    count = 0
    #list to store the first index where the needle is
    list = []
    for x in range(len(haystack)):
        #stores x for fun
        e = x
        for i in range(len(needle)):
            #idk what m doing here but it's working :D
            if e < len(haystack):
                if haystack[e] == needle[i]:
                    e += 1
                else: 
                    break
                if i == len(needle)-1:
                    list += [str(x)]
                    count += 1
    if count == 0:
        return -1
    #can't i just use find function and get done with it :d
    print("it was found on these list of index : " + str(tuple(list)))
    print("the length of the string is :"+ str(len(haystack)))
    return "number of times found = " + str(count) + "\n"


print(strsstr("ABCDCDC", "CDC"))
