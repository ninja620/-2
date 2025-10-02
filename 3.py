def is_prime(number):
    d=2
    while d*d<=number:
        print(d*d)
        if number%d==0:
            return False
        d+=1
    return True


number=int(input())
print(is_prime(number))
