def isPrime(N):
    for i in range(2,int(N**0.5)+1):
        if N%i==0:
            return False
    return True

def primeGenerator(M):
    result= [2,3]
    maxn= M//6
    n=1
    while n<=maxn:
        a= 6*n - 1
        if isPrime(a):
            result.append(a)
        b= 6*n + 1
        if b>=M:
            break
        else:
            if isPrime(b): result.append(b)
        n+=1
    return result

def main():
    print(primeGenerator(100))


if __name__ == "__main__":
    main()