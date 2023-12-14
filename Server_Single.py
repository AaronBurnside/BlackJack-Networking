import socket
import itertools
import random
import threading
import time
import re

def shuffle_deck():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)
    return deck

def Deal_Card(Deck, Deck_Size):
        selector = random.choice(range(0,Deck_Size))
        Card = Deck[selector]
        Deck.remove(Card)
        Deck_Size -= 1
        return Card

def run_server():
    deck = shuffle_deck()
    Deck_Size = len(deck)
    # create a socket object
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "127.0.0.1"
    port = 5555

    # bind the socket to a specific address and port
    server.bind((server_ip, port))
    # listen for incoming connections
    server.listen(0)
    print(f"Listening on {server_ip}:{port}")

    # accept incoming connections
    client_socket, client_address = server.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

    request = client_socket.recv(1024)
    request = request.decode("utf-8") # convert bytes to string
    while True:    
        if request.lower() == "close":
            # send response to the client which acknowledges that the
            # connection should be closed and break out of the loop
            client_socket.send("closed".encode("utf-8"))
            return
        if request.lower() == "join":
            x = Deal_Card(deck, Deck_Size)
            Deck_Size -= 1
            client_socket.send(f'{x[0]}'.encode("utf-8"))
            Dealer_Card = Deal_Card(deck, Deck_Size)
            print(Dealer_Card)
            Deck_Size -= 1
           
            Dealer_Total =  Dealer_Card[0]
            break
        else:
            print(f"Received: {request}")
            response = "Incompatible command".encode("utf-8") # convert string to bytes
            # convert and send accept response to the client
            client_socket.send(response)

    while True:
        request = client_socket.recv(1024)
        request = request.decode("utf-8") # convert bytes to string
        if request.lower() == "hit":
            x = Deal_Card(deck, Deck_Size)
            Deck_Size -= 1
            client_socket.send(f'{x[0]}'.encode("utf-8"))
            if Dealer_Total <= 16:
                Dealer_Card = Deal_Card(deck, Deck_Size)
                print(Dealer_Card)
                Deck_Size -= 1
                Dealer_Total += Dealer_Card[0]
            else:
                print("The Dealer has Stood")
        elif request.lower() == "stand":
            response = "Total".encode("utf-8")
            client_socket.send(response)
            time.sleep(3)
            request = client_socket.recv(1024)
            request = request.decode("utf-8") # convert bytes to string
            total = int(request)
            if Dealer_Total > 21:
                if total <= 21:
                    response = f'The Dealer busted and you have won'.encode("utf-8")
                elif total > 21:
                    response = f'it is a tie you both busted'.encode("utf-8")
            elif total > Dealer_Total and total <= 21:
                response = f'You have won over a {Dealer_Total}'.encode("utf-8")
            elif total > 21 and Dealer_Total <= 21:
                response = f'You have busted and the dealer has won with a {Dealer_Total}'.encode("utf-8")
            elif Dealer_Total > total and Dealer_Total <= 21:
                 response = f'you have lost to a {Dealer_Total}'.encode("utf-8")
            client_socket.send(response)
            break

        else:
            print(f"Received: {request}")
            response = "Incompatible command".encode("utf-8") # convert string to bytes
            # convert and send accept response to the client
            client_socket.send(response)

    # close connection socket with the client
    client_socket.close()
    print("Connection to client closed")
    # close server socket
    server.close()


run_server()