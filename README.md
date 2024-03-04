# ED-MS
Microservice works by using text files as the pipeline, in order to interact request data from the microservices you must print the the callto.txt file "playerID,#ofGames" Ex. "12,10" 

The microservice then reads and clears the request, collects the data and prints the output into output.txt in JSON format, your main py can just wait until the file is not empty and then read and clear it. 


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
