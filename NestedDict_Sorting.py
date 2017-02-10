import operator
from operator import itemgetter

list = []

#List embedded in values() of Dictionary in Python
x = {"ted": [True,4,3], "barney": [False,4,3], "lily": [True,3,1], "robin": [True,4,1], "marshall": [True,4,0]}


#To custom-sort specified data columns, dict is converted to list
for each in x.keys():
    sublist = [each, x[each][1], x[each][2]]
    list.append(sublist)

#sort the list
sorted_1 = sorted(list, key=lambda x: int(x[1]),reverse = True)


#print the out the first largest UNIQUE n values
i=0
n = 2
while i<=n:    
    print(sorted_1[i][0] + " " + str(sorted_1[i][1]))
    i += 1

    try: 
        if sorted_1[i][1] == sorted_1[i+1][1]: 
            n += 1
    except: 
        pass