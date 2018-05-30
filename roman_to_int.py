def roman_to_int():
    try:
        l1={'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'X':10,'XI':11,'XII':12,'XIII':13,'XIV':14,'XV':15,'XVI':16,'XVII':17,'XVIII':18,'XIX':19,'XX':20};
        #l1.setdefault("invalid_value");
        r_num=raw_input("Enter Roman Value");
        print(l1[r_num]);
    except:
        print("enter valid value")

roman_to_int()
