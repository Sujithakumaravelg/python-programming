try:
        def camelcase():
            s1=raw_input()
            a=s1.split(' ')
            g=" "
            for i in range(0,len(a)):
                    a[i]=a[i].capitalize()
            c=a[0]
            for i in range(1,len(a)):
                    c=c+g+a[i]
            print c
        camelcase()
except:
	print "Enter Valid Value"
