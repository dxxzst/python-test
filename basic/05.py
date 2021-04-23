a = 0
b = 1
for x in range(50):
    (a, b) = (b, a + b)
    print('%d:%d' % (x, a), end='\n')
