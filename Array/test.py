data =[[[1,2],[3,4]],[[5,6],[7,8]]]


def func(m):
    v = m[0][0]
    for row in m:
        for element in row:
            if v<element: v=element
            
    return v


print(func(data[0]))


fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]
     
fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'
     
sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20
    
print(sum)