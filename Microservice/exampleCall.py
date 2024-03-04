while 1:
    f = open("callto.txt", "w")
    playerID = int(input("Which Player?\n1) Stephen Curry\n2) Draymond Green\n3) Klay Thompson\n"))
    numGames = int(input("How Many Games?\n"))

    # Print to text file in format as "playerID,numGames" Ex. 2,5
    string = str(playerID) + "," + str(numGames)

    f.write(string)
    f.close()


    output = open("output.txt", 'r')

    done = output.read()

    # Wait for output to not be empty
    while not done:
        done = output.read()
    output.close()

    # Print output and clear file
    print(done)
    open("output.txt", 'w').close()





