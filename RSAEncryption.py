import random

def RSAencryption(string, strength) :
    # Walks through the steps to encrypt a string with an encryption strength

    # Creates the two primes to use to encrypt
    randPrimeList = CreateRandOrderPrime(strength)
    prime1 = randPrimeList[0]
    prime2 = randPrimeList[1]
    modulus = prime1 * prime2
    phi = (prime1-1)*(prime2-1)
    RandCoprimeList = RandCoprime(phi)
    publicKey = [RandCoprimeList[0], modulus]
    privateKey = [CreatePriv(publicKey[0],phi,RandCoprimeList)[0], modulus]
    # Represents string as numbers to be encrypted
    stringNumRep = []
    for x in string :
        stringNumRep.append(ord(x))
    # Encrypts the string using the Public Key and the FastMod algorithm
    encryptedString = []
    for x in stringNumRep :
        encryptedString.append(FastMod(x,publicKey[0],publicKey[1]))
    # Decrypts the string using the Private Key and the FastMod algorithm
    decryptedString = []
    for x in encryptedString :
        decryptedString.append(FastMod(x,privateKey[0],privateKey[1]))
    # Converts the num back into a string
    decryptedWord = ""
    for x in decryptedString :
        decryptedWord += chr(x)
    # Creates text for user
    print("Original String: " + string)
    print("Converts the string into a list: ", end="")
    print(stringNumRep)
    print("Creates a Public Key to encypt the string: ", end="")
    print(publicKey)
    print("Encrypts the string using the Public Key: ", end="")
    print(encryptedString)
    print("Creates a Private Key to decrypt the string: ", end="")
    print(privateKey)
    print("Decrypts the string using the Public Key: ", end="")
    print(decryptedString)
    print("The final decrypted word is: " + decryptedWord)

def RandCoprime(num) :
    # Returns the Coprime List of num shuffled
    CoprimeList = []
    for x in range(3, num) :
        if (GCD(x, num) == 1) :
            CoprimeList.append(x)
    random.shuffle(CoprimeList)
    return CoprimeList

def CreatePriv(key, cPhi, coList) :
    # Returns the Private Key using the public key, Phi, and the Coprime list
    privList = []
    for x in coList :
        if ((x * key) % cPhi == 1) :
            privList.append(x)
    random.shuffle(privList)
    return privList

def CreateRandOrderPrime(topLimit) :
    # Returns a list of primes in a random order using the Sieve of Eratosthenes
    if (topLimit < 3) :
        print("topLimit must be at least 3")
        return []
    primeList = []
    for x in range(topLimit+1) :
      primeList.append(x)
    for p in range(2,len(primeList)) :
      multiply = 2
      while (primeList[p] != 0 and (p * multiply < len(primeList))) :
          primeList[p * multiply] = 0
          multiply+=1
    index = len(primeList) - 1
    while index >=0 :
         if (primeList[index] == 0) :
              del primeList[index]
         index-=1
    del primeList[0]
    random.shuffle(primeList)
    return primeList

def GCD(a,b) :
    # Returns the greatest common denominator of two numbers
    if (b == 0) :
        return a
    return GCD(b, a % b)


def FastMod(base, exp, mod) :
    # Fast Modulus algorithm to do base ** exp % mod very quickly

    # Converts exp into its binary decomposition
    expDecomp = []
    num = 0
    while (exp > 0):
        if exp % 2 == 1:
            expDecomp.append(num)
        exp = exp // 2
        num += 1
    
    # Calculates the mod of the powers of two less than exp
    n = 0
    exponAdd = []
    while (n <= expDecomp[len(expDecomp)-1]) :
        if (n == 0) :
            exponAdd.append(base**(2**n) % mod)
        else :
            exponAdd.append(exponAdd[n-1]*exponAdd[n-1] % mod)
        n+=1

    # Use modular multiplication properties to combine the calculated mod values
    finalSum = 1
    for x in expDecomp :
        finalSum*=exponAdd[x]
    return finalSum % mod

RSAencryption("Hello World",999)