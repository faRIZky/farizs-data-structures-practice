text_num1 = "dataprocessing123"
# change into data123

'''
slicing the list

slice the list ainto parts and we want to combine it

- get the first word --> data
- get the second word --> 123
- combine the words

slicing --> start : end : step

data --> 0 : 4 : 1
123 --> 15 ::1
'''
# print(text_num1[0:4:1] + text_num1[14::1])

text_num2 = "openAIisCool"
'''
expected output = siIAlooC

reversed = looCsiIAnepo 

Cool --> start : 11 , stop : 7, step : -1 
AI --> start : 5, stop : 3, step : -1
is --> start : 7, stop : 5
'''

text_num2_reversed = text_num2[::-1]
# print(text_num2[7:5:-1] + text_num2[5:3:-1] + text_num2[11:7:-1])

text_num3 = "abcdefghijklmno"
'''
expected output = aceonmlk

2 pieces of words
- ace
- onlmk

ace = 0 : 5 : 2
onmlk --> reversed --> 14 : -6 : -1
'''

# print(text_num3[0:5:2] + text_num3[-1:-6:-1])

text_num4 = "abracadabra123"

'''
expected = cadabarba

cadab --> 3:9:1
arba --> reversed --> -7: -4 : -1

'''
text_num4_reversed = text_num4[::-1]
# print(text_num4[4:9:1] + text_num4 [-4:-8:-1])

# or --> manual dulu --> reverse
# print(text_num4 [-7:-3:1][::-1]) --> arba

text_num5 = "123pythonista"

'''
expected = python13t

python --> 3 : 9
13 --> 0: 3 : 2
t --> 5  OR 5 : 4 : -1 OR -2:-3:-1  
'''

# print(text_num5[3:9:1] + text_num5[0:3:2] + text_num5[5:4:-1])
# print(text_num5[3:9:1] + text_num5[0:3:2] + text_num5[-2:-3:-1])

'''
print(text_num5[5:4:-1]) --> kalo backwards, maka stopnnya + 1. kalo biasa kan berarti angka stopnya -1, ini jika stopnya ga minus ygy. intinya kalo stop dan step beda tanda, maka berbalik jg dari hukum awal
'''
text_num6 = text = "foundation"

'''
expected = fudnoita

fud = 0 : 6 : 2

noita = -1:-6:-1 ---> sama-sama minus step dan stopnya
'''

# print(text_num6[0:6:2] + text_num6[-1:-6:-1])

text_num7 = "imagination"
'''
expected = igamioit

imagi --> reverse --> [0:5:1][::-1]
tio ---> reverse ---> [-4:-2:-1]
'''

# print(text_num7[0:5:1][::-1] + text_num7[-4:-1:1][::-1])

text_num8 = "understanding"

'''
expected = red n st dn

- positve slicing
- negative slicing

[start : stop : step] --> -1
- red? --> [2: 5 : 1][::-1] --> red
- n --> [1]
- st --> [5:7:1]
- dn --> [1: 3 : 1] [::-1]
'''

print(text_num8[2: 5 : 1][::-1]+text_num8[1]+text_num8[5:7:1]+text_num8[1: 3 : 1] [::-1])
