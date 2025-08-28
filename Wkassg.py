#Empty List 
my_list = []

# append element 10 - 40
for i in range(10, 41, 10):
    my_list.append(i)
   
# Insert 15 at 2nd position
my_list.insert(1, 15)
print(my_list)

# Joining the 2 list using extend method
list_2 = [70, 60, 50]
my_list.extend(list_2)

#pop thelast value
my_list.pop()

#arrange in ascending order using sort
my_list.sort()

#find index of 30 and print it
position = my_list.index(30)
print(position)

print(my_list)
