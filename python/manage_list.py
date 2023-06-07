if __name__ == '__main__':
    N = int(input("Enter the number of commands you'll be passing : "))
blist = []
for x in range(0, N):
    blist.append(input("enter a command : "))
ll = list(blist)
ll = [item.split() for item in ll]
xlist = []

for i in ll:
    if i[0] == "insert":
        index = int(i[1])
        element = int(i[2])
        xlist.insert(index, element)
        pass
    if i[0] == "print":
        print(xlist)
        pass
    if i[0] == "remove":
        xlist.remove(int(i[1]))
        pass
    if i[0] == "append":
        element = int(i[1])
        xlist.append(element)
        pass
    if i[0] == "sort":
        xlist = sorted(xlist, key=int)
        pass
    if i[0] == "pop":
        xlist.pop()
        pass
    if i[0] == "reverse":
        xlist.reverse()
        pass
    
