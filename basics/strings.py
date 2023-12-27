greet = 'Hi! '
greet = greet * 5

print(greet)
name = 'imtiaz'
greeting_sentence =  f'Hi! I am {name}, your personal assistant'
ord = ord('s')
char = chr(ord)

print(name not in greeting_sentence)

print(f'this will return ascii number of character \s {ord}')
print(f'this will return character at ascii code {ord} which is {char}')
print(f'length of greet variable is {len(greet)} and its type is {type(greet)}')

print(str(ord))
#inexing of string variables
print(f'length of variable \'greeting_sentence\' is {len(greeting_sentence)} and at index -{len(greeting_sentence)} is character {greeting_sentence[-len(greeting_sentence)]}')
#string slicing
print('String Slicing \n')
print(len(name))
print(name[0:2])
print(name[-6:-4])
#skips substring known as striding
print(name[0:7:3])
#reverse striding
print(name[6:0:-2])
#reversing whole string via striding method
print(name[::-1])
#strings are immutable , following are ways to replace character in a string
name = name[:1] + 'n' + name[2:]
print(name)
name = name.replace('n','m')
print(name)
#bultin methods, methods is attached to an object, like name.replace(), and function is not attached, like len(name)

print(name.capitalize())
print(name.upper())
print(name.swapcase())
print(name.swapcase())
print(name.lower().capitalize())
print(name.center(8,'~'))