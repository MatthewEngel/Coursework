#Matthew Engel and Tro Davenport

# Aquired very basic code from Dr.El-Tawab
# read up on sockets at https://www.geeksforgeeks.org/socket-programming-python/
#At the end of our assignment, the final issue we faced was a repeatedly
#sending and receiving from client to server and back. We could only
#achieve this exchange once. We consulted Chat GPT, and it pointed out we were
#missing a single while loop in our server code. 

import socket		 	                                      # Import socket module
import datetime   
def solution(message_to_send):
    try:
       result = eval(message_to_send)  
       return result, True
    except Exception as e:
        return f'error: {e}', False                            # imports datetime

def server1():
    server = socket.socket() 	  		                       # Create a socket object
    port = int(input("What Port do you wish to connect to?"))  # Reserve a port for your service.
    open_ip = socket.gethostbyname(socket.gethostname())
    print(open_ip)
    server.bind((open_ip, port)) 			                   # Bind to the port, server listens to ay potential IP's. 
    server.listen(5) 			                               # Allows for 5 (or less) connections at once.
    print('server is up. Port to connect to is: ' + str(port))

    try:
        while True:
            client_info, addr = server.accept() 		       # Establish connection with client.
            print ('Client IP and port:', addr, port, '\n')    # Print the IP address and port of the connected client
            
            while True:  
                potential_sentinel = client_info.recv(1024).decode()   # 1024 bytes o' data max.
                if potential_sentinel == 'finished':                   # if message is sentinel:
                    client_info.close()                                # Close the connection.
                    break
                
                message_to_send = str('Message received, time: ' + str(datetime.datetime.now()) + ', thank you! \n')
                result, is_math = solution(potential_sentinel)
                if is_math:
                    message_to_send = (f'{message_to_send}the solution is: {result} \n')
                else:
                    message_to_send = (f'{message_to_send}\n{result} \n')                #if not sentinel, send this.
                client_info.send(message_to_send.encode())                                          #sends this.


     
    except KeyboardInterrupt:
        server.close()
        print('server closed.')
if __name__ == "__main__":
    server1()