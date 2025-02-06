import threading
import socket

server_ip="0.0.0.0"
server_port=8080

def main():
    
    server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(server_ip, server_port)
    server.listen(5)
    print(f"[!] Listening on {server_ip}:{server_port}")
    
    while True:
        client,address= server.accept()
        print(f"Accepted connection from {address[0]}:{address[1]}")
        client_handler= threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"[!] Received: {request.decode('utf-8')}")
        sock.send(b'ACK')
        
main()        
        
        