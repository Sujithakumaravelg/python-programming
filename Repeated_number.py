class Repeated_number:
    def repeated_value():
        list1=[]
        final_list=[]
        N=int(input("enter N"))
        for i in range(0,N):
            val=int(input())
            list1.append(val)
        print(list1)
        for num in range(len(list1)):
            i = num + 1
         
            for i in range(i, len(list1)):
                if list1[num]== list1[i]:
                    final_list.append(list1[num])
        if len(final_list)==0:
            print("unique")
        else:
            final_list.sort()
            print(final_list)

    repeated_value()
