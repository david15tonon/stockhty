from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18], 
     ['Wed',15,21,20,19],['Thu',11,20,22,21], 
     ['Fri',18,17,23,22],['Sat',12,22,20,18], 
     ['Sun',13,15,19,16]]) 
m = reshape(a,(7,5)) 
i=0
while(i<len(m)):
    
    print(m[i])
    i+=1
    
# ----------------------------------------------------------#
print('\n* Inserting new element to each columns:\n')

new_column = []
for i in range(0, len(m)):
    new_column.append(m[i][1] + m[i][3])
    print(append(m[i], m[i][1] + m[i][3]))

m_c = insert(m, [5], new_column, axis=1)

print(m_c)