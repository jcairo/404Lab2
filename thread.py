import socket
import threading


class TCP_Connection(object):
    """Reps a tcp connection"""
    def __init__(self, client_socket, server_socket):
        self.client_socket = client_socket
        self.server_socket = server_socket

def worker(tcp_connection):
    # process request
    buffer = ''
    receiving = 1
    while receiving:
        data = tcp_connection.client_socket.recv(1024)
        tcp_connection.client_socket.sendall('Hello {0}.\r\nClose Connection (y/n)?\r\n'.format(data))
        print data
        if data.strip() == 'y':
            tcp_connection.client_socket.sendall('Goodbye\r\n')
            receiving = False
    tcp_connection.client_socket.close()

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Created Socket'
    sock.bind(('', 8080))
    sock.listen(5)
    threads = []
    while 1:
        (client_socket, address) = sock.accept()
        print address
        tcp_connection = TCP_Connection(client_socket, sock)
        t = threading.Thread(target=worker, args=(tcp_connection,))
        threads.append(t)
        t.start()

