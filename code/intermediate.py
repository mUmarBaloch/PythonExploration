x,y =30,40
#short hand if else
print('x is greater') if x > y else print('y is greater')
#short hand if
if 0==0 : print('true condition')
a = 330
b = 380
print("A") if a > b else print("=") if a == b else print("B")

#and or not , pass

if 1>2 or 2==2:
    if 2==2 and 3==3:
            pass
else :
    print('false')

# loops while and for is already discussed!!
    
# functions
def function1(*params,name  = 'samar'):
     print(f'student name is {name} and student age is ',params[1])
#return type and parameter type doesnt play important role, becuase python a dynamic language
def function2(age,name:str,scores:list[int],**param) -> int:
     print(f"{name}\'s age is {age}, from  {param['city']}, {param['institute']} \n his score in subjects is {scores} ")

function1(22,33)

function2(22,'umar',[88,67,89,45],institute='university of sindh',city='mirpur khas')

#lamda , its anonnymous function with multiple parameters and single expression :- lamda parameter : expression

x = lambda count : count * 2

print(x(2))