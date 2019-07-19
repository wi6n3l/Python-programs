my_list=['a','b','a','b','c','b','d','b','e','f']
for item in sorted(set(my_list)):
    count=my_list.count(item)
    print(str(item)+" = "+str(count)+ 'times')
