import socket 
import sys 
import time

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "127.0.0.1" 
    server_port = 5555
    total = 0 
    client.connect((server_ip, server_port))
    msg = input("Choose to Join, or Close: ")
    client.send(msg.encode("utf-8")[:1024])
    time.sleep(2)
    print(msg.lower)
    if msg == "join":
        response = client.recv(1024)
        response = response.decode("utf-8")
        print(f"The First Card you recieved was: {response}")
        val = int(response)
        print(val)
        total = val
        print(total)

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
    else:
        response = client.recv(1024)
        response = response.decode("utf-8")
        if response.lower() == "closed":
            client.close()
            print("Connection to server closed")
            return
        else: 
            print(f'Recieved: {response}')



    while True:
        # input message and send it to the server
        msg = input("Choose to Hit or Stand: ")
        client.send(msg.encode("utf-8")[:1024])

        # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")

        # if server sent us "closed" in the payload, we break out of the loop and close our socket
        if response.lower() == "closed":
            break
        if response.lower() == "total":
            msg = (total)
            client.send(f'{msg}'.encode("utf-8")[:1024])
            time.sleep(5)
            response = client.recv(1024)
            response = response.decode("utf-8")
            print(response)
            break

        print(f"The Card you recieved was: {response}")
        val =int(response)
        print(val)
        print(total)
        total = total + val



    # close client socket (connection to the server)
    client.close()
    print("Connection to server closed")


run_client()