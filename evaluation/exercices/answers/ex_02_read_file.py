count = 0

f = open('nameslist.txt', 'r')
#text = f.read()
#print(text)

while 1:
    text = f.read(10000)
    if not text: break
    count += text.count('\n')

count += 1
print(count)

f.close