import socket
import itertools
import random
import os
import threading

def shuffle_deck():
    deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
    random.shuffle(deck)
    return deck
class SERVER:
    Deck = list()
    players = 0
    server_ip = "127.0.0.1"
    port = 5555
    flag = False
    Deck_Size = 0
    clients = set()
    Results = set()
    p = 0 
    def __init__(self):
        self.Deck = shuffle_deck()
        self.Deck_Size = len(self.Deck) - 1

    def Deal_Card(self):
        selector = random.choice(range(0,self.Deck_Size))
        Card = self.Deck[selector]
        self.Deck.remove(Card)
        self.Deck_Size -= 1
        return Card


    def start_server(self):
        
        clients_lock = threading.Lock()


        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            self.server.bind((self.server_ip, self.port))
            self.server.listen(4)
            print(f"Listening on {self.server_ip}:{self.port}")
            clients_lock.acquire()


            while self.players <= 3 and self.flag == False:
                client_socket, client_address = self.server.accept()
                print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
        
                thread = threading.Thread(target= handle_client, args=(self, client_socket, client_address,))
                thread.start()
            clients_lock.release()
            for c in self.clients:
                    x = self.Deal_Card
                    c[0].send(x.encode("utf-8"))
            while self.p < self.players: 
                clients_lock.acquire()
                client_socket, client_address = self.server.accept()
                clients_lock.release()
                thread = threading.Thread(target= handle_game, args=(self, client_socket, client_address,))
                thread.start()
            a = 1
            for c in self.Results:
                Dealers_Num = random.choice(range(12,21))
                if int(c[1]) > Dealers_Num and int(c[1]) <= 21:
                    print(f"{c[0]} has won")
                
                #if a + 1 <= len(self.Results):
                    #if int(c[1]) > (self.Results[a])[1] and int(c[1]) <= 21:
                       # Winner = c[0]
                    #else:
                       # Winner = self.Results[a]
                
            


        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.server.close()
        

def handle_game(Server, client_socket, addr):
    try: 
        Server.clients_lock.acquire()
        while True:
            request = client_socket.recv(1024).decode("utf-8")
            print(f"Received: {request}")
            if request.lower == "hit":
                C = Server.Deal_Card
                client_socket.send(C.encode("utf-8"))
            if request.lower == "stand":
                client_socket.send("Total".encode("utf-8"))
            else:
                Server.Results.add([ addr, request])
                Server.p += 1
                break
        Server.clients_lock.release()



    
    except Exception as e:
        print(f"Error when hanlding client: {e}")
    finally:
        client_socket.close()
        print(f"Connection to client ({addr[0]}:{addr[1]}) closed")



def handle_client(Server, client_socket, addr):
        try:
            while True:
                print("A1")
                # receive and print client messages
                request = client_socket.recv(1024).decode("utf-8")
                print(f"Received: {request}")
                if request.lower() == "close":
                    client_socket.send("closed".encode("utf-8"))
                    break
                elif request.lower() == "join":
                    print("A2")
                    Server.players += 1
                    Server.clients.add([client_socket, addr])
                    #client_socket.send("Game has been Joined".encode("utf-8"))
                elif request.lower() == "start":
                    Server.flag = True
                    break
                else:
            # convert and send accept response to the client
                    response = "accepted"
                    client_socket.send(response.encode("utf-8"))
            print("A3")
            Server.clients_lock.acquire()
            client_socket.send("starting".encode("utf-8"))
            Server.clients_lock.release()

        except Exception as e:
            print(f"Error when hanlding client: {e}")
        finally:
            client_socket.close()
            print(f"Connection to client ({addr[0]}:{addr[1]}) closed")

            


The_server =  SERVER
print(The_server.server_ip)
print("Start")
The_server.start_server(The_server)
print("hello")
