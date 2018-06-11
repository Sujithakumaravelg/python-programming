def prime_num():
    try:
        n=0
        l=int(input())
        r=int(input())
        for num in range(l,r+ 1):
           if num > 1:
               for i in range(2,num):
                   if (num % i) == 0:
                       break
               else:
                   n=n+1
        print(n)          
    except:
        print("enter valid value")
prime_num()
