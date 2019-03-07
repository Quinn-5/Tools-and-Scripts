src = 'primes1.txt' # str(input("What is the path to the input file?\n"))
dest = 'primes.txt' # str(input("What is the path to the output file?\n"))

replacement = str.maketrans(' ', '\n')
with open(src) as f:
    start = f.readlines()
f.close

length = start.__len__()

temp = open(dest, 'w')
temp.write('')
temp.close

for j in range (0, length):
    print(str(j) + ' out of ' + str(length))
    tempTable = []
    for k in start[j]:
        if k == ' ':
            tempTable.append(k.translate(replacement))
        else:
            tempTable.append(k)
    with open(dest, 'a') as f:
        for item in tempTable:
            f.write(item)

# This section opens the file and deletes all empty lines 
with open(dest) as f:
    start = f.readlines()

length = start.__len__()
i=0
while i < length:
    print(str(i) + ' out of ' + str(length))

    if start[i] == '\n':
        del start[i]
    else:
        i += 1
    if i+1 == length:
        break
    length = start.__len__()

with open(dest, 'a') as f:
    for items in start:
        f.write(items)