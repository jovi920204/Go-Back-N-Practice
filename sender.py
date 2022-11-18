import socket
import time

HOST = '127.0.0.1'
PORT = 8000
server_addr = (HOST, PORT)

send_base = 0
next_seq_num = 0

cwnd_size = 3
num_pkt = 10

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while (send_base < num_pkt):
    for i in range(0,cwnd_size):
        if (send_base+i < num_pkt):
            next_seq_num = send_base+i
            clientMessage = str(next_seq_num)
            client.sendto(clientMessage.encode(), server_addr)
    client.settimeout(5)
    try:
        serverMessage, addr = client.recvfrom(1024)
        print('server message is:', serverMessage.decode("utf-8"))
        send_base += 1
    except Exception as e:
        print('timeout')
        # the codes to handle the timeout event
        for i in range(0,cwnd_size):
            if (send_base+i < num_pkt):
                next_seq_num = send_base+i
                clientMessage = str(next_seq_num)
                client.sendto(clientMessage.encode(), server_addr)