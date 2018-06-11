def prime_num():
    try:
        l=int(input())
        r=int(input())
        for num in range(l,r+ 1):
           if num > 1:
               for i in range(2,num):
                   if (num % i) == 0:
                       break
               else:
                   print(num)
    except:
        print("enter valid value")
prime_num()
