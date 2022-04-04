a = input('enter a string').upper()
dictionary = {}
ltrList = []



for i in a:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1

print ("Dictionary :\n " +  str(dictionary))

b = input('choose a letter').upper()

if b in dictionary:
    freq = dictionary.get(b)
    print('Frequency count of that letter:', str(freq))
    del dictionary[b]
    print ("Dictionary after that letter removed: :",  str(dictionary))

    for key in dictionary.keys():
        ltrList.append(key)

    ltrList.sort()
    print('Letters sorted:', str(ltrList))

else:
    print('Letter not in dictionary')
