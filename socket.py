import socket
EOL1 = '\n\n'
EOL2 = '\n\r\n'
body = '''Hello, world! <h1> from My first socket web server </h1>'''
response_params = [
	'HTTP/1.0 200 OK',
	'Date: Thu, 31 Dec 2019 01:01:01 GMT',
	'Content-Type: text/plain; charset=utf-8',
	f'Content-Length: {len(body)}\r\n',
	body,
]
response = '\r\n'.join(response_params)
print(response)

def handle_connection(conn, addr):
	request = ""
	while EOL1 not in request and EOL2 not in request:
		request += str(conn.recv(1024))
	print(request)
	conn.send(response)
	conn.close()


def main():
    # socket.AF_INET    用于服务器与服务器之间的网络通信
    # socket.SOCK_STREAM    基于TCP的流式socket通信
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次Ctrl C之后，快速再次重启
	serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	serversocket.bind(('127.0.0.1', 8080))
    # 可参考：https://stackoverflow.com/questions/2444459/python-sock-listen
	serversocket.listen(1)
	print('http://127.0.0.1:8080')

	try:
		while True:
			conn, address = serversocket.accept()
			handle_connection(conn, address)
	finally:
		serversocket.close()


if __name__ == '__main__':
	main()
