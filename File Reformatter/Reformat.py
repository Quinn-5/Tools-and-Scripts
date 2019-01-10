# This replaces all spaces with newlines

replacement = str.maketrans(' ', '\n')
with open('primes1.txt') as f:
Primes = f.readlines()
print(Primes)

length = Primes.__len__()

i = 0
while i < length:
    print(str(i) + ' out of ' + str(length))

    for j in range (0, Primes.__len__()):
        tempTable = []
        for k in Primes[j]:
            if k == ' ':
                tempTable.append(k.translate(replacement))
            else:
                tempTable.append(k)
        Primes[j] = tempTable


    if Primes[i] == '\n':
        del Primes[i]
    else:
        i += 1
    if i+1 == length:
        break
    length = Primes.__len__()

go = bool(input("Would you like to overwrite the output file"))

if not go:
    return

temp = open('primes.txt', 'w')
temp.write('')

with open('primes.txt', 'a') as f:
    for item in Primes:
        f.write(item)

Print(Primes)


# This section opens the file and deletes all empty lines 
with open('primes1.txt') as f:
    Primes = f.readlines()
print(Primes)

length = Primes.__len__()

for i in range(0, length):
    if i+1 == length:
        break
    print(str(i) + ' out of ' + str(length))
    if Primes[i] == '\n':
        del Primes[i]
    length = Primes.__len__()
with open('primes.txt', 'a') as f:
    for item in Primes:
        f.write(item)

print(Primes)
