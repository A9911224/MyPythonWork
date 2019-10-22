# coding: utf-8

def date(y,m,d):
    ans = False
    if (m == 1 or m ==3 or m ==5 or m ==7 or m ==8 or m ==10 or m ==12) and 1<=d and d<=31:
        ans = True
    elif (m ==4 or m ==6 or m ==9 or m ==11) and 1<=d and d<=30:
        ans = True
    elif y%400==0 and m==2 and 1<=d and d<=29:
        ans = True
    elif y%100==0 and m==2 and d==29:
        ans = False
    elif y%4!=0 and m==2 and 1<=d and d<=28:
        ans = True    
    elif y%4==0 and m==2 and 1<=d and d<=29:
        ans = True  
    else:
        ans = False
    return ans

a = input("年：")
b = input("月：")
c = input("日：")
        
        
date(int(a),int(b),int(c))
