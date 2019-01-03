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
