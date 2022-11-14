import random

for i in range(26):
    for j in range(26):
        print(chr(i + 65) +" "+chr(j + 65) +" "+ str(10 + random.randrange(100)))

text = 'Learn from yesterday, live for today, hope for tomorrow.'

matrix = [[0] * 26 for i in range(26)]
for t in range(len(text) - 1):
    if ord(text[t]) < 97 or ord(text[t]) > 122:
        continue
    if ord(text[t+1]) < 97 or ord(text[t+1]) > 122:
        continue
    matrix[ord(text[t])-97][ord(text[t+1])- 97]+=1
    print(text[t]+" "+ text[t+1])

#print(matrix)
#for i in range(26):
#    for j in range(26):
        #if matrix[i][j] >= 1:
        #print(chr(i + 97) + " "+chr(j + 97)+" "+str(matrix[i][j]))
        #print(chr(i + 97) + " "+chr(j + 97)+" "+str(random.randrange(100) + 10))
