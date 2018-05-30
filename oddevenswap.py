try:
    def oddevenswap(st):
        s = list(st)
        for c in range(0,len(s),2):
            t=s[c];
            s[c]=s[c+1];
            s[c+1]=t;

        print("".join(s));
    i=raw_input("Enter Str");
    oddevenswap(i);
except:
    print("enter valid value");
