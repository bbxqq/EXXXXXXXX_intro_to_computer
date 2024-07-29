import socket
#Fibonacci
def fibonacci(n):
    f = [0, 1]
    if n == 0:
        return f[0]
    if n == 1:
        return f[1]
    for i in range(2, n+1):
        f.append(f[i - 1] + f[i - 2])
    return f[n]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#綁定ip跟host
server_socket.bind(('0.0.0.0', 8000))
# 開始監聽
server_socket.listen(1)
print('Waiting for connection…')
# 接受連接
client_socket, client_address = server_socket.accept()
print('add connection from', client_address)

while True:
    # 接收數據
    data = client_socket.recv(4096)
    if data.decode() == 'exit':
        print('conection closed')
        server_socket.close() #關閉連線
        break
    else:
        print('Received from', client_address, ':', data.decode())
        # 發送數據
        ans = fibonacci(int(data.decode()))
        client_socket.sendall(str(ans).encode())
        print('Send to', client_address, ':', (str(ans).encode()).decode())

    # 關閉連接
    #client_socket.close()
    #server_socket.close()