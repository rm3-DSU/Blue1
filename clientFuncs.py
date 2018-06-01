def addClient(clientIP):
    file = open("clients.txt","a+")
    file.write(clientIP+"%d\r\n")
    file.close()

def listClients():
    file = open("clients.txt","r")
    cline = file.readlines()
    for x in cline:
        print (x)    
    file.close()     

def sendClients():  
    # retrieve all clients from list and send to each client
    # so all clients "know" about eachother
    # will build out once client / server issues are resolved

def sendCommand(command, clientIP):
    # send a command to a client
    # will build out once client / server issues are resolved

def requestFile(file, clientIP):
    # request a file from a client
    # will build out once client / server issues are resolved

def sendFile(file, clientIP):
    # send a file from the server to the client
    # will build out once client / server issues are resolved