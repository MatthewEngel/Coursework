#Matthew Engel and Tro
#March 23 2024
#Due 03/26/2024
#Sources:

#Copied this script off of Professor El-Tawabs 13th slide initially.
# read up on sockets at https://www.geeksforgeeks.org/socket-programming-python/
#At the end of our assignment, the final issue we faced was a repeatedly
#sending and recieving from client to server and back. We could only
#acheive this exchange once. We consulted Chat GPT, and it pointed out we were
#missing a single while loop in our server code.
#side note: Chatgpt also suggested a lot of try catches to avoid code crashing.
#We didn't apply these suggested changes, but it was good information learn.

from socket import *

def client():
    ip_Adress = input("what IP Adress do you wish to connect to?")
    server_Port = int(input('What port do you wish to connect to?'))
    print('ip used: ' + str(ip_Adress) + '. Port used: ' + str(server_Port) + '.')
    print('\nWhen done, type \'finished\'.')
    sentinel_value = 'finished'                    #value to disconect.
    clientSocket = socket(AF_INET, SOCK_STREAM)    #creates a socket for funnsies
    clientSocket.connect((ip_Adress, server_Port)) #connects to the desired server who is constantly searching for client.


    #asks user for value to either end charades or send sentence to server.

    while True:   
        sentence = input('Input a math equation to solve: ')   #asks user for another value to send or end code.
                    #while the user has not inputed sentinel value, the charade continues.
        if sentence == sentinel_value:
            break
        clientSocket.send(sentence.encode())         #encodes and sends sentence
        print('From Server:', clientSocket.recv(1024).decode())    #prints the sentence back from server
        

    clientSocket.send(sentence.encode())             #sends this so server can close its socket
    print('sentinel detected, closing socket')       
    clientSocket.close()                             #closes client socket


if __name__ == "__main__":
    client()
