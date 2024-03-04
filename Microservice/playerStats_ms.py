from pymongo import MongoClient

client = MongoClient("localhost", 27017)
nba_db = client.NBAStats
gameStats = nba_db.gamestats


while 1: 
    f = open("callto.txt", 'r')
    boolE = False 
    concact = ""
    cct2 = ""

    char = f.read(1)

    # Waits til there is contents in file
    while not char:
        char = f.read(1)

    # Concacts the input into 2 variables
    while 1:
        if not char: 
            break

        if char == ',':
            boolE = True 
        elif boolE == False: 
            concact += char
        else:
            cct2 += char
        char = f.read(1)

    # Puts concacts into variables
    playerID = concact
    inputNum = int(cct2)

    finalOutput = []

    # Retrieve matched game stats for player, append the to array
    for game in gameStats.find():
        if playerID == game['player_id']:
            finalOutput.append(game)
            if len(finalOutput) >= inputNum:
                break

    # Output to output.txt
    f.close()
    output = open("output.txt", 'w')
    output.write(str(finalOutput))
    output.close()
    open('callto.txt', 'w').close()
