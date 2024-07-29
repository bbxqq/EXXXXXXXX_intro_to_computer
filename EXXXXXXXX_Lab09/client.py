import socket

# 創建套接字
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連接到伺服器
server_ip = '192.168.137.1'
server_port = 8000
client_socket.connect((server_ip, server_port))
print('connect to',server_ip)

while True:
    n = input('The Fibonacci(n) when n = ')
    # 關閉連接
    if n == 'exit':
        print('close client_socket')
        client_socket.sendall(str(n).encode())
        client_socket.close()
        break
    else:
        # 發送數據
        client_socket.sendall(str(n).encode())
        # 接收數據
        data = client_socket.recv(4096)
        print('the ans is', data.decode())