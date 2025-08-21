my_list = []
print("list1:",my_list)
print("Before append: ", my_list)
#using append method
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("After append: ", my_list)
my_list.insert(2,15)
print(my_list)

my_list2 = [50, 60, 70]
print("my_list2:",my_list2)

#join two lists
my_list.extend(my_list2)

print("After extend: ", my_list)

my_list.remove(70)
print("After remove: ", my_list)

my_list.sort()
print("After sort: ", my_list)
ind = my_list.index(30)
print("index of 30 = ", ind)



