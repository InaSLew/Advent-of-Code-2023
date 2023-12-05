CONSTRAINT = {
    'red': 12,
    'green': 13,
    'blue': 14
}

with open("input.txt") as f:
    games = f.read().split("\n")
    idSum = 0
    for game in games:
        meta = game.split(':')
        id = int(meta[0].split(' ')[1])
        print(id)
        possible = True
        for round in meta[1].split(';'):
            print(round)
            for pair in round.strip().split(', '):
                splitPair = pair.split(' ')
                if (CONSTRAINT[splitPair[1]] < int(splitPair[0])):
                    possible = False
                    break
            if (possible == False):
                break
        
        if (possible):
            idSum += id
    
    print(idSum)
