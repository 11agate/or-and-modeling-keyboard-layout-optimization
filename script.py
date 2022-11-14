import random

numberOfKeys = 26
numberOfKeys = 4
inputText = 'Learn from yesterday, live for today, hope for tomorrow.'

def generatePositionSet():
    result = str()
    for i in range(numberOfKeys):
        result += chr(65 + i) + ' '
    with open('data/positionSet.dat', 'w') as f:
        f.write('set Position := ' + result[:-1] + ';')

def generateKeySet():
    result = str()
    for i in range(numberOfKeys):
        result += chr(97 + i) + ' '
    with open('data/keySet.dat', 'w') as f:
        f.write('set Key := ' + result[:-1] + ';')

def generateRandomPositionCost():
    result = str()
    for i in range(numberOfKeys):
        for j in range(numberOfKeys):
            result += "  "+chr(65+i) +" "+chr(65+j) +" "+ str(10 + random.randrange(100)) + '\n'
    with open('data/positionCost.dat', 'w') as f:
        f.write('param PositionCost :=\n' + result[:-1] + ';')

def generateRandomKeyMove():
    result = str()
    for i in range(numberOfKeys):
        for j in range(numberOfKeys):
            result += "  "+chr(97+i) +" "+chr(97+j) +" "+ str(10 + random.randrange(100)) + '\n'
    with open('data/keyMove.dat', 'w') as f:
        f.write('param KeyMove :=\n' + result[:-1] + ';')

def generateKeyMoveFrom(text = 'Learn from yesterday, live for today, hope for tomorrow.'):
    result = str()
    matrix = [[0] * 26 for i in range(26)]
    for t in range(len(text) - 1):
        if ord(text[t]) < 97 or ord(text[t]) > 97+numberOfKeys-1:
            continue
        if ord(text[t+1]) < 97 or ord(text[t+1]) > 97+numberOfKeys-1:
            continue
        matrix[ord(text[t])-97][ord(text[t+1])- 97]+=1
    
    for i in range(26):
        for j in range(26):
            if matrix[i][j] >= 1:
                result += "  "+ chr(i + 97) + " "+chr(j + 97)+" "+str(matrix[i][j])+'\n'
    with open('data/keyMove.dat', 'w') as f:
        f.write('param KeyMove :=\n' + result[:-1] + ';')

generatePositionSet()
generateKeySet()
generateRandomPositionCost()
generateRandomKeyMove()
#generateKeyMoveFrom()
