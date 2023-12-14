# Overview

i created a client server blackjack game in which after launching the server a client program can be run which will connect and allow you to play against a dealer on the server

the purpose of creating this game was to explore the inner workings and difficulties of networking

[Software Demo Video](https://youtu.be/XGoXHviLzUc)

# Network Communication

I used a client / server architecture and alongside TCP on port 5555
The message formats being sent by the client to the server where always in the form of commands where as the messages sent by the server to the client vary depending on the sitation usual just being an number

# Development Environment

this software was developed completely in visual studios

I used the Python language along with the following libraries 
socket 
itertools
threading
time
re

# Useful Websites

* [Programiz](https://www.programiz.com/python-programming/examples/shuffle-card)
* [Data Camp] (https://www.datacamp.com/tutorial a-complete-guide-to-socket-programming-in-python)
* [Stack Overflow](https://stackoverflow.com/questions/27139240/i-need-the-server-to-send-messages-to-all-clients-python-sockets)
* [Python Threading Library](https://docs.python.org/3/library/threading.html)
* [Tutorials point](https://www.tutorialspoint.com/How-to-get-integer-values-from-a-string-in-Python)
* [Real Python](https://realpython.com/python-sockets/)
* [Geeks for Geeks](https://www.geeksforgeeks.org/socket-programming-python/)
* [Web Site Name](http://url.link.goes.here)



# Future Work
* complete the threading for the multiplayer version
* Display the dealers total to the user as the game progresses
* allow the user to start a new game without exiting the program