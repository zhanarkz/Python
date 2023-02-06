n = '22 * 300 - 14 + 10 * 10'
m = n.split()
m2 = []

def calculation(a, b, ch):
    if ch == '+':
        return a+b
    elif ch == '-':
        return a-b
    elif ch == '/':
        return a/b
    elif ch == '*':
        return a*b

# a = int(m[0])
# c = m[1]
# b = int(m[2])


result = 0

for i in range (1, len(m) -1, 2):
    if m[i] == '*' or m[i] == '/':
        result = calculation(int(m[i-1]), int(m[i +1]), m[i])
        m2.append(result)
    else:
        m2.append(m[i])
        m2.append(int(m[i+1]))


#print(m[i], m[i+1])
print(m2)
print(result)



    
