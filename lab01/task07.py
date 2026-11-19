numbr = int(input('Ведите число >>> '))
numbr = abs(numbr)

n0 = numbr % 10
n1 = numbr % 100 // 10
n2 = numbr % 1000 // 100
n3 = numbr // 1000

sm = n0 + n1 + n2 + n3

new = n0*1000+n1*100+n2*10+n3

print(n3)
print(n2)
print(n1)
print(n0)
print(sm)
print(new)