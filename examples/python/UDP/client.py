import socket

# Создаем UDP-сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Отправляем сообщение серверу
s.sendto(b"Hello, Server", ('127.0.0.1', 8888))

# Закрываем сокет
s.close()
