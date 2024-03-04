# ED-MS
Grabs data from mongodb and returns it to main in json format.
# UML Diagram

![image](https://github.com/kotacodes/ED-MS/assets/46253336/f8889292-7632-4c91-bf66-2bf27adbd00b)


# Example Request
```
# Print to text file in format as "playerID,numGames" Ex. 12,10
    string = str(playerID) + "," + str(numGames)

    f.write(string)
    f.close()
```

# Example Output Call 
```
output = open("output.txt", 'r')

    done = output.read()

    # Wait for output to not be empty
    while not done:
        done = output.read()
    output.close()

    # Print output and clear file
    print(done)
    open("output.txt", 'w').close()
```
