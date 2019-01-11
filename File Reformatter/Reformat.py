def  main(): 
    replacement = str.maketrans(' ', '\n')
    with open('primes1.txt') as f:
        Primes = f.readlines()
    f.close

    print(Primes)

    length = Primes.__len__()

    temp = open('primes.txt', 'w')
    temp.write('')
    temp.close
    
    i = 0
    file = open('primes.txt', 'a')

    for j in range (0, length):
            print(str(j) + ' out of ' + str(length))
            tempTable = []
            for k in Primes[j]:
                if k == ' ':
                    tempTable.append(k.translate(replacement))
                else:
                    tempTable.append(k)
            # Primes[j] = tempTable
            with open('primes.txt', 'a') as f:
                for item in tempTable:
                    f.write(item)
    
 

    # This section opens the file and deletes all empty lines 
    with open('primes.txt') as f:
        Primes = f.readlines()

    print(Primes)
   
    length = Primes.__len__()
    i=0
    while i < length:
        print(str(i) + ' out of ' + str(length))

        if Primes[i] == '\n':
            del Primes[i]
        else:
            i += 1
        if i+1 == length:
            break
        length = Primes.__len__()


    
    with open('primes.txt', 'a') as f:
        for items in Primes:
            f.write(item)





    print(Primes)

main()