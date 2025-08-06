my_list = [];

my_list.append(10);
my_list.append(20);
my_list.append(30);
my_list.append(40);
#print("list: ", my_list);
my_list.insert(1, 15);  
#print("list: ", my_list);
my_list.extend([50, 60, 70])
#print("list: ", my_list);
my_list.pop();
#print("list: ", my_list);
my_list.sort();
#print("list: ", my_list);
print(my_list.index(30));
