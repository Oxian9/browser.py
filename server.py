import socket

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8080

# Create socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(1)
    print(f'Listening on port {SERVER_PORT} ...')

    while True:
        # Wait for client connections
        client, client_address = s.accept()
        print(f"{client_address} has connected!")

        # Get the client request
        with client as c:
            request = c.recv(1024).decode()
            print(request)

            # Send HTTP response
            response = """ \n
<!DOCTYPE html>
<html>
<body>

<h1>Chinese Delights</h1>

<p>Welcome. Take a look at our menu!</p>
<img src="https://i.redd.it/8jr9b7af44e41.jpg" alt="quotev.com" width="700" height="700">
<img src="https://i2.wp.com/ordinarypatrons.com/wp-content/uploads/2019/12/Jia-Wei-Restaurant-Roxy-1.jpg?resize=644%2C483&ssl=1" alt="quotev.com" width="644" height="483">
<img src="https://chinachannel.co/wp-content/uploads/2015/09/menu3.png" alt="quotev.com" width="900" height="500">
<p>When ready please signal to our staff to order.</p>


</body>
</html>

"""
            #send response to client
            c.sendall("HTTP/1.1 200 OK".encode())
            c.sendall(response.encode())