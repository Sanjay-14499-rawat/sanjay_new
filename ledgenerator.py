##l=[0B0110,0B1001,0B1111,0B1001,0B1001]
##for e in l:
##     n=0
##     c=0b1000
##     while n<4:
##          z=e&c
##          
##          if z==0:
##               print('.',end='')
##          else:
##               print('O',end='')
##          c=c>>1
##          n+=1
##     print()




##l=[0B0110,0B1001,0B1111,0B1001,0B1001]
##print(l)
test_list = [0,1,1,0]
print("the ori list"  + str(test_list))
r=int("".join(str(x) for x in test_list),2)
print(str(r))
































