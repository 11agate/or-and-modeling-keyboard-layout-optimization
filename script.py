import random

numberOfKeys = 26
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

blockList = [
    ['Q','A','Z'],
    ['W','S','X'],
    ['E','D','C'],
    ['R','F','V','T','G','B'],
    ['Y','H','N','U','J','M'],
    ['I','K'],
    ['O','L'],
    ['P'],
]

def getBlockNumber(position: str) -> int:
    for i in range(len(blockList)):
        for j in range(len(blockList[i])):
            if position == blockList[i][j]:
                return j

def generatePositionCost():
    result = str()
    for i in range(numberOfKeys):
        for j in range(numberOfKeys):
            bi = getBlockNumber(chr(65+i))
            bj = getBlockNumber(chr(65+j))
            score = 0
            if bi == bj:
                score = 0
            elif bi - bj == -5:
                score = 6
            elif bi - bj == -4:
                score = 4
            elif bi - bj == -3:
                score = 1
            elif bi - bj == -2:
                score = 5
            elif bi - bj == -1:
                score = 3
            elif bi - bj == 1:
                score = 2
            elif bi - bj == 2:
                score = 4
            elif bi - bj == 3:
                score = 1
            elif bi - bj == 4:
                score = 3
            elif bi - bj == 5:
                score = 5
            result += "  "+chr(65+i) +" "+chr(65+j) +" "+ str(score * 10)+ '\n'
    with open('data/positionCost.dat', 'w') as f:
        f.write('param PositionCost :=\n' + result[:-1] + ';')

def generateBlockCost():
    result = str()
    txt = ['L1', 'L2', 'L3', 'L4', 'R1', 'R2', 'R3', 'R4']
    for bi in range(8):
        for bj in range(8):
            score = 1
            if bi == bj:
                score = 5
            elif abs(bi - bj) == 1:
                score = 2
            elif abs(bi - bj) == 2:
                score = 3
            elif abs(bi - bj) == 3:
                score = 4
            result += "  "+ txt[bi]+" "+ txt[bj] +" "+ str(score * 10)+ '\n'
    with open('data/blockCost.dat', 'w') as f:
        f.write('param BlockCost :=\n' + result[:-1] + ';')

def generateRandomKeyMove():
    result = str()
    for i in range(numberOfKeys):
        for j in range(numberOfKeys):
            result += "  "+chr(97+i) +" "+chr(97+j) +" "+ str(10 + random.randrange(100)) + '\n'
    with open('data/keyMove.dat', 'w') as f:
        f.write('param KeyMove :=\n' + result[:-1] + ';')

def generateKeyMoveFrom(text = 'Learn from yesterday, live for today, hope for tomorrow.'):
    text = 'In many applications, we are concerned only with a subset of all ordered pairs from two sets. For example, in the transportation model, shipments may not be possible from every origin to every destination. The shipping costs per unit may be provided only for the usable origin-destination pairs, so that it is desirable to index the costs and the variables only over these pairs. In AMPL terms, we want the set LINKS defined above to contain just a subset of pairs that are given in the data, rather than all pairs from ORIG'
    
    with open('input') as f:
        
        text = f.read()
    result = str()
    state = str()
    matrix = [[0] * 26 for i in range(26)]
    for t in range(len(text) - 1):
        if ord(text[t]) < 97 or ord(text[t]) > 97+numberOfKeys-1:
            continue
        if ord(text[t+1]) < 97 or ord(text[t+1]) > 97+numberOfKeys-1:
            continue
        matrix[ord(text[t])-97][ord(text[t+1])- 97]+=1
    
    li = []
    for i in range(26):
        for j in range(26):
            if matrix[i][j] >= 1:
                li.append([matrix[i][j], i, j])
#                result += "  "+ chr(i + 97) + " "+chr(j + 97)+" "+str(matrix[i][j])+'\n'
#                state += "  "+ chr(i + 97) + " "+chr(j + 97) + '\n'
  
    li = sorted(li, key=lambda x: -x[0])
    
    for l in range(min(60, len(li))):
        i = li[l][1]
        j = li[l][2]
        result += "  "+ chr(i + 97) + " "+chr(j + 97)+" "+str(matrix[i][j])+'\n'
        state += "  "+ chr(i + 97) + " "+chr(j + 97) + '\n'
        
    with open('data/keyMove.dat', 'w') as f:
        f.write('param KeyMove :=\n' + result[:-1] + ';')
    with open('data/keyState.dat', 'w') as f:
        f.write('set UsingKeys :=\n' + state[:-1] + ';')

def runAMPL():
    generatePositionSet()
    generateKeySet()

    #generateRandomPositionCost()
    generatePositionCost()

    #generateRandomKeyMove()
    generateKeyMoveFrom()
    
    generateBlockCost()

    import subprocess
    import time

    start = time.time()

    result = subprocess.run(["ampl_mswin64/ampl.exe","script.run"], capture_output=True, text=True)
    with open('logs/log', 'w') as f:
        f.write(result.stdout)

    t = time.time() - start
    print(t)


generatePositionSet()
generateKeySet()

#generateRandomPositionCost()
generatePositionCost()

#generateRandomKeyMove()
generateKeyMoveFrom()

generateBlockCost()

runAMPL()
