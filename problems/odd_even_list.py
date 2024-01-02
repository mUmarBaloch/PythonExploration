mix_list= [7,14, 3, 19, 12, 5, 18, 8, 2, 10]

order = [x for x in mix_list if x % 2 ==0] +[x for x in mix_list if x % 2 !=0]


print(order)