digits = [2,4,2,4,6,9]
#[print(x) for x in digits]
x = 0
while(x<len(digits)):
    print(digits[x])
    x +=1

list = [y for y in digits if 2 != y]
print('\n',list,'\n')

range_list = [b for  b in range(0,20)]
print(range_list)

duplicate_list  = list

print('original ',list )
list = list.remove(4)
print('duplicate ', duplicate_list)


#tuples are unchangeable which means we canot change specific index element, and ordered.

tuple_list = (1,4,2,1)
print(type(tuple_list),tuple_list)

tuple_list = (2,5)
print(type(tuple_list))
print(tuple_list[1])
#unpacking a tuple
(student_class,student_age) = tuple_list
print(student_age,' ', student_class)
# * asteric for unpacking, if values are grrater than no of variables, it will assign remaining elements to * variable
tuple_list = ('apple','gauva','pomegranate','tomato','some more pomegranates','orange')
(green,*red,vitamin_c) = tuple_list
print(red)
[print(x) for x in tuple_list if 'a' in x]
print(tuple_list *2)

#sets  unordered, unchangeable ,(can add and update), no duplicates allowed

this_set = {'umar',22,'university of sindh'}
this_set2 = {'samar',23,'university of sindh'}
print(this_set.intersection(this_set2))

#dictionaries ❤️

my_dictionary = {
    'name':'umar baloch',
    'age': 22,
    'institute': 'university of sindh',
    'campus' : 'mirpurkhas',
    'checkingValueDuplicates':'umar baloch'
}

print(my_dictionary['name'])
[print(x) for x in my_dictionary.values()]

my_dictionary = dict(name = 'samar',age= 23, institute= 'university of sindh')
print(my_dictionary)
#checks if key in dictionary exist
if 'institute' in my_dictionary:
    print('yes this is a key')
#we can add new or update key with same thing 
my_dictionary.update({'name':'umar'})
#here we will add new key 
my_dictionary.update({'father_name':'dawood'})
print(my_dictionary)
#adding new key with another method
my_dictionary['surname']='baloch'
print(my_dictionary)
#deleting last key
my_dictionary.popitem()
print(my_dictionary)
#removing selected key
my_dictionary.pop('father_name')
print(my_dictionary)
#displaying both keys and values

for x,y in my_dictionary.items():
    print(x,y)


