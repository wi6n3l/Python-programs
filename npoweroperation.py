n=int(input("Enter number of operations:"))
a=[]
for i in range (0,n):
    s=raw_input("Input operation numbers:")
    l=s.split(' ')
    a.append(l)
for i in range (0,n):
    p=1
    #print a
    for j in range (0,int(a[i][1])):
        p*=int(a[i][0])
    print p
