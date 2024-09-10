   #Matthew Engel and Tro
#March 23 2024
#Sources:

#Copied this script off of Professor El-Tawabs 13th slide initially.
# read up on sockets at https://www.geeksforgeeks.org/socket-programming-python/
#At the end of our assignment, the final issue we faced was a repeatedly
#sending and recieving from client to server and back. We could only
#acheive this exchange once. We consulted Chat GPT, and it pointed out we were
#missing a single while loop in our server code. 

#REPORT:
#The client throws the error 111 "connection refused" since there is no server up and running with that IP adress.
#Other errors included 133 no route to host
#Solution: set up try catch to avoid this error.


import socket		 	                                   # Import socket module
import datetime   
def solution(message_to_send):
    try:
       result = eval(message_to_send)  
       return result, True
    except Exception as e:
        return f'error: {e}', False                                       # imports datetime

def server1():
    server = socket.socket() 	  		                        # Create a socket object
    port = int(input("What Port do you wish to connect to?"))  # Reserve a port for your service.
    open_ip = socket.gethostbyname(socket.gethostname())
    print(open_ip)
    server.bind((open_ip, port)) 			                       # Bind to the port, server listents to ay potential IP's. 
    server.listen(5) 			                               # Allows for 5 (or less) connections at once.
    print('server is up. Port to connect to is: ' + str(port))

    try:
        while True:
            client_info, addr = server.accept() 		                       # Establish connection with client.
            print ('Client IP and port:', addr, port, '\n')                       # Print the IP address and port of the connected client
            
            while True:  
                potentian_sentinel = client_info.recv(1024).decode()                # 1024 bytes o' data max.
                if potentian_sentinel == 'finished':                  # if message is sentinel:
                    client_info.close()                                    # Close the connection.
                    break
                
                message_to_sends = str('Message received, time: ' + str(datetime.datetime.now()) + ', thank you! \n')
                result, is_math = solution(potentian_sentinel)
                if is_math:
                    message_to_send = (f'{message_to_send}the solution is: {result} \n')
                else:
                    messae_to_send = (f'{message_to_send}\n{result} \n')                #if not sentinel, send this.
                client_info.send(message_to_send.encode())                                          #sends this.


     
    except KeyboardInterrupt:
        server.close
        print('server closed.')
if __name__ == "__main__":
    server1()