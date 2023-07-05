import sys
import socket
import datetime
import threading

def currentTime():
    now = datetime.datetime.now()
    formattedTime = now.strftime("%H:%M:%S")
    return formattedTime

def send(sock):
    while threadFlag:
        try:
            message = input()
            deleteLastLine()
            sock.send(message.encode("utf8"))
        except:
            print("An error occured while trying to send a message!")
            break

def receive(sock):
    while threadFlag:
        try:
            message = sock.recv(2048).decode()
            if message:
                print("[{}] {}".format(currentTime(), message))
            else:
                break
        except:
            print("An error occured while trying to reach the server!")
            break
        
def deleteLastLine():
    cursorUp = "\x1b[1A"
    eraseLine = "\x1b[2K"
    sys.stdout.write(cursorUp)
    sys.stdout.write(eraseLine)

def main():
    global threadFlag
    host = "localhost"
    port = 25001
    
    socketFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    clientSocket = socket.socket(socketFamily, socketType)
    clientSocket.connect((host, port))
    
    sendingThread = threading.Thread(target=send, args=(clientSocket,))
    receivingThread = threading.Thread(target=receive, args=(clientSocket,))

    receivingThread.start()
    sendingThread.start()
    
    while receivingThread.is_alive() and sendingThread.is_alive():
        continue
    threadFlag = False
    
    clientSocket.close()
    print("\nYou can now close the application.")

threadFlag = True

if __name__ == "__main__":
    main()
    pass