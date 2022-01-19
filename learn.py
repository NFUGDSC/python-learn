# output
print('hello world')
print("hello world")
print('hello'+'world')
print('hello','world')
print('hello','world'*2)

# python data type
print(type(1))
print(type('1'))
print(type(['1','2']))

# declare
x=1
y='hello'

# input
x=input('input:')
print(type(x))
print(x)

# calu
x=10
print(x)
x=x-1
print(x)
x-=1
print(x)
print(x)

#boolen
print(bool(0))
print(bool(False))
print(bool('False'))
print(bool(True))
print(bool('True'))
print(bool(1))
print(bool(0.1))
print(bool('hello'))
print(bool(None))

# len
print(len('hello world'))

# condition
print(1==2)
print(1>2)
print(1<2)
print(1<=2)
print(1>=2)
print(1!=2)

# while
x=2
while x:
    print(x)
    x=x-1

# if
a=1
if a==1:
    print(1)
elif a==2:
    print(2)
else:
    print(a)

# for
for i in range(5):
    print(i)
for j in range(1,6):
    print(j)
for k in range(1,6,2):
    print(k)
for l in range(6,1,-1):
    print(l)
for m in range(len('hello')):
    print(m)

# string
a='hello world'
print(a)
print(a[0])
print(a[1])
for m in range(len(a)):
    print(a[m])

# list
a=[1,2,3]
print(a)
a.append(4)
print(a)
a+=[5,6]
for i in a:
    print(i)

# char to ascii
a='a'
print(a)
a=ord('a')
print(a)

# ascii to char
a=97
print(97)
a=chr(a)
print(a)

# ord vs int
print(int('a'))
print(ord('a'))
print(int('1'))
print(ord('1'))
