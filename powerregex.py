import re
n=int(input("Enter number of operations:"))
a=[]
for i in range (0,n):
    s=raw_input("Input operation numbers:")
    a.append(re.search('(\d+) (\d+)',s))
    #a.append(d)
for i in range (0,n):
    p=1
    print a.groups()
    #for j in range (0,a[i][1]):
        #p*=a[i][0]
    #print p

