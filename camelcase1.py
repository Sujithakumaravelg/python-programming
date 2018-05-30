def camelcase():
    s=raw_input()
    if(len(s)<=1000000):
        a=s.split(' ')
        g=" "
        for i in range(0,len(a)):
                    a[i]=a[i].capitalize()
        c=a[0]
        for i in range(1,len(a)):
                    c=c+g+a[i]
        print c
    else:
        print("Enter Valid Value")
camelcase()

